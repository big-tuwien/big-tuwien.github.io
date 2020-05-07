import json
import os
import re

import bibtexparser
import requests
import frontmatter
import urllib.request
import shutil
import yaml
import xmltodict
import datetime

BIG_TID = 4760
BIG_OID = 18460477

LECTURE_EXERCISE_COURSE_TYPES = ['VO', 'VU']
SEMINAR_PROJECT_COURSE_TYPES = ['SE', 'PV', 'PR']

TEMPLATE_DIR = 'templates'

DATA_DIR = '../data'
CONTENT_DIR = '../content'
PEOPLE_DIR = CONTENT_DIR + '/people'
TEACHING_DIR = CONTENT_DIR + '/teaching'
PUBLICATION_DIR = CONTENT_DIR + '/publication'

TISS_BASE = 'https://tiss.tuwien.ac.at'
PUBLIK_BASE = 'https://publik.tuwien.ac.at'
PEOPLE_URL = f'{TISS_BASE}/api/orgunit/v22/id/{BIG_TID}?persons=true'
PROJECTS_ONGOING_URL = f'{TISS_BASE}/api/pdb/rest/projectsearch/v2?instituteOid={BIG_OID}&status=1'
PROJECTS_FINISHED_URL = f'{TISS_BASE}/api/pdb/rest/projectsearch/v2?instituteOid={BIG_OID}&status=2'
COURSE_LECTURER_URL = TISS_BASE + '/api/course/lecturer/{}'
PUBLICATION_URL = f'{PUBLIK_BASE}/pubexport.php'
BIBTEX_URL = f'{PUBLIK_BASE}/pubbibtex.php'


def _id(name):
    return name.lower().replace(' ', '-').replace('ö', 'oe').replace('ä', 'ae').replace('ü', 'ue')\
        .replace('ß', 'sz').replace(' ', '')


def _get_semesters(at=datetime.datetime.now(), summer_term_start=3, winter_term_start=10):
    # figure out current semester
    if at.month < summer_term_start or at.month >= winter_term_start:
        term = 'W'
        year = at.year
        # january 2020 -> 2019W
        if at.month < summer_term_start:
            year -= 1
    else:
        term = 'S'
        year = at.year

    current = f'{year}{term}'

    # get the past semester
    if term is 'W':
        term = 'S'
    else:
        term = 'W'
        year -= 1

    prev = f'{year}{term}'

    return current, prev


def load_courses(lecturers, semester=None, session=requests.Session()):
    course_dict = {}

    namespaces = {
      f'{TISS_BASE}/api/schemas/course/v10': None,
      f'{TISS_BASE}/api/schemas/hasCourse/v10': None,
      f'{TISS_BASE}/api/schemas/i18n/v10': None
    }

    for lect in lecturers:
        url = COURSE_LECTURER_URL.format(lect['oid'])
        query = {}
        if session:
            query['semester'] = semester
        r = session.get(url, params=query)
        xml_dict = xmltodict.parse(r.content, encoding='utf-8', process_namespaces=True, namespaces=namespaces)

        # skip invalid users
        if 'tuvienna' not in xml_dict:
            continue
        parse_res = xml_dict['tuvienna']
        # skip users that are not associated to any courses
        if 'course' not in parse_res:
            continue

        for course in parse_res['course']:
            # skip cases where xml deserialization oddly does not generate a dict
            if not isinstance(course, dict):
                continue
            course_id = f'{course["courseNumber"]}-{course["semesterCode"]}'
            # skip duplicates
            if course_id in course_dict:
                continue
            course_dict[course_id] = dict(course)

    return list(course_dict.values())


def parse_courses(courses, people):
    lectures_exercises = [c for c in courses if c['courseType'] in LECTURE_EXERCISE_COURSE_TYPES]
    seminars_projects = [c for c in courses if c['courseType'] in SEMINAR_PROJECT_COURSE_TYPES]
    other = [c for c in courses if c['courseType'] not in (LECTURE_EXERCISE_COURSE_TYPES + SEMINAR_PROJECT_COURSE_TYPES)]

    result = {}

    for identifier, courses in [('lectures_exercises', lectures_exercises), ('seminars_projects', seminars_projects), ('other', other)]:
        result[identifier] = [{
            'authors': [p['identifier'] for p in people if str(p['oid']) in course['lecturers']['oid']],
            'number': course["courseNumber"],
            'url': course["url"],
            'type': course["courseType"],
            'title': course["title"]["en"]
        } for course in courses]

    return result


def load_publications(researchers, session=requests.Session()):
    publications = []

    for res in researchers:
        query = {'zuname': res['last_name'], 'vorname': res['first_name'], 'inst': 'E194', 'abt': '03', 'func': '1'}
        r = session.get(PUBLICATION_URL, params=query)
        content = r.content.decode('ISO-8859-1')
        xml = xmltodict.parse(content, encoding='utf-8')['export']  # get root element
        if 'publikation' not in xml:
            continue
        result = xml['publikation'] if type(xml['publikation']) is list else [xml['publikation']]
        publications.extend(result)

    return publications


def parse_publications(publications, bib_db, author_transform_map):
    type_map = {
        'Dissertation': 'diss_dipl',
        'Wissenschaftlicher Bericht': 'bericht',
        'Zeitschriftenartikel': 'zeitschriftenartikel',
        'Vortrag mit Tagungsband': 'vortrag_poster_mit_tagungsband',
        'Vortrag ohne Tagungsband': 'vortrag_poster_ohne_tagungsband',
        'Diplom- oder Master-Arbeit': 'diss_dipl',
        'Buch-Herausgabe': 'buch_herausgabe',
        'Monographie (Erstauflage)': 'buch',
        'Monographie (Folgeauflage)': 'buch',
        'Beitrag in elektron. Zeitschrift': 'elektron_zeitschrift',
        'Buchbeitrag': 'buchbeitrag',
        'Beitrag in Tagungsband': 'beitrag_tagungsband',
        'Vortrag mit CD- oder Web-Tagungsband': 'vortrag_poster_mit_cd_tagungsband',
        'Herausgabe eines Bandes einer Buchreihe': 'herausgabe_buchreihe',
        'Beitrag in CD- oder Web-Tagungsband': 'beitrag_cd_tagungsband',
        'Haupt-(Keynote-)Vortrag mit Tagungsband': 'vortrag_poster_mit_tagungsband',
        'Haupt-(Keynote-)Vortrag ohne Tagungsband': 'vortrag_poster_ohne_tagungsband',
        'Posterpräsentation mit Tagungsband': 'vortrag_poster_mit_tagungsband',
        'Posterpräsentation ohne Tagungsband': 'vortrag_poster_ohne_tagungsband',
        'Posterpräsentation mit CD- oder Web-Tagungsband': 'vortrag_poster_mit_cd_tagungsband',
    }

    academic_type_map = {
      'article': 2,
      'book': 5,
      'inbook': 6,
      'incollection': 6,
      'inproceedings': 1,
      'manual': 4,
      'mastersthesis': 7,
      'misc': 0,
      'phdthesis': 7,
      'proceedings': 0,
      'techreport': 4,
      'unpublished': 3,
      'patent': 8
    }

    posts = []

    for pub in publications:
        pub_id = pub['pub_id'].lower()
        pub_type = pub['type']

        if pub_type in type_map:
            pub_type = type_map[pub_type]
        else:
            print(f'Unknown Type: {pub_type} @ {pub_id}')
            continue

        # get abstract and strip all <br> tags
        abstract = pub['abstract_englisch'] if 'abstract_englisch' in pub else ''
        abstract = re.sub('<br/?>', '', abstract)
        # remove all dots from title (intention is to remove trailing dots)
        title = pub['titel'].strip('.')
        authors = pub['autor_info'] if ',' in pub['autoren_clean'] else [pub['autor_info']]
        authors = [f'{a["vorname_lang"]} {a["nachname"]}' for a in authors]
        authors = [author_transform_map[name] if name in author_transform_map else name for name in authors]
        pdf_link = pub['link_pdf'] if 'link_pdf' in pub else ''
        publik_link = pub['infolink'].replace('&lang=1', '&lang=2')

        year = ''
        month = '01'
        day = '01'
        if 'datum_von' in pub[pub_type]:
            dateparts = pub[pub_type]['datum_von'].split('.')
            if len(dateparts) >= 3:
                day, month, year = dateparts[0], dateparts[1], dateparts[2]
            else:
                year = dateparts[0]
        elif 'jahr' in pub[pub_type]:
            year = pub[pub_type]['jahr']

        bib_entry = None
        for entry in bib_db.entries:
            if entry['ID'].lower() == pub_id:
                bib_entry = entry
                break
        academic_type = academic_type_map.get(bib_entry["ENTRYTYPE"], 0) if bib_entry else 0

        # create the post
        post = frontmatter.Post(content='', title=title, authors=authors, date=f'{year}-{month}-{day}',
                                publishDate=f'{year}-{month}-{day}', publication_types=[str(academic_type)],
                                abstract=abstract, featured=False, url_pdf=pdf_link,
                                links=[{'name': 'Publik', 'url': publik_link}])

        posts.append((pub_id, post))

    return posts


def load_bibtex(publishers, session=requests.Session()):
    composite_bibtex = ''

    for pub in publishers:
        query = {'zuname': pub['last_name'], 'vorname': pub['first_name'], 'inst': 'E194', 'abt': '03', 'func': '1'}
        r = session.get(BIBTEX_URL, params=query)
        result = r.content.decode('ISO-8859-1')
        for line in result.split(os.linesep):
            if len(line) == 0 or line.startswith('BibTeX-Export:') or line.endswith('ausgegeben') or line.startswith('@comment'):
                continue
            composite_bibtex += line + '\n'
        composite_bibtex += '\n'

    return composite_bibtex


def parse_bibtex(bibtex):
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.customization = bibtexparser.customization.convert_to_unicode
    parser.ignore_nonstandard_types = False
    bib_database = bibtexparser.loads(bibtex_str=bibtex, parser=parser)

    return bib_database


def save_publications(posts, bib_db, pub_dir):
    for identifier, post in posts:
        directory = f'{pub_dir}/{identifier}'

        # create folder
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            continue

        bib_entry = None
        for entry in bib_db.entries:
            if entry['ID'].lower() == identifier:
                bib_entry = entry
                break

        if bib_entry:
            db = bibtexparser.bibdatabase.BibDatabase()
            db.entries = [bib_entry]
            writer = bibtexparser.bwriter.BibTexWriter()
            with open(f'{directory}/cite.bib', 'w+', encoding='utf-8') as f:
                f.write(writer.write(db))

        with open(f'{directory}/index.md', 'w+', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))


def main():
    # load config
    with open('config.yml', 'r', encoding='utf-8') as yml:
        try:
            config = yaml.safe_load(yml)
        except yaml.YAMLError as e:
            print('Cannot read config.yml: ', e)
            return

    s = requests.Session()

    print('Fetching people. Creating files for new people in the "content/authors" directory')

    # fetch people
    r = s.get(PEOPLE_URL)
    data = r.json()
    people = data['employees']

    # add short names
    for person in people:
        person['identifier'] = _id(person['first_name'] + ' ' + person['last_name'])

    # apply whitelist
    print('Applying people whitelist')
    whitelist = [_id(name) for name in config['people']['whitelist']]
    people = [p for p in people if p['identifier'] in whitelist]

    for person in people:
        first_name = person['first_name']
        last_name = person['last_name']
        name = f'{first_name} {last_name}'
        directory = f'{PEOPLE_DIR}/{person["identifier"]}'

        # create folder
        if not os.path.exists(directory):
            print(f'Creating author files for {name}')
            os.makedirs(directory)
        else:
            print(f'Skipping {name} ({person["identifier"]}) - profile already exists')
            continue

        # download profile pic or copy default
        pic_dest = directory + '/avatar.jpg'
        if person['picture_uri']:
            urllib.request.urlretrieve(TISS_BASE + person['picture_uri'], pic_dest)
        else:
            shutil.copyfile(TEMPLATE_DIR + '/authors/user/avatar.jpg', pic_dest)

        # apply metadata to markdown front matter
        post = frontmatter.load(TEMPLATE_DIR + '/authors/user/_index.md')
        post['name'] = name
        post['authors'] = [person["identifier"]]
        post['role'] = person['preceding_titles']
        post['email'] = person['main_email']
        pairs = [{'key': 'Mail', 'value': person["main_email"], 'link': f'mailto:{person["main_email"]}'}]
        if person['main_phone_number']:
            pairs.append(
                {'key': 'Phone', 'value': person["main_phone_number"], 'link': f'tel:{person["main_phone_number"]}'}
            )
        post['pairs'] = pairs
        with open(f'{directory}/_index.md', 'w+', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))

    with open(f'{DATA_DIR}/people.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(people, indent=4))

    # fetch courses. has to be done separately for each person (fetching courses for the institute returns an empty set)
    print('Fetching courses. Creating files for courses in the "content/teaching" directory')

    current_semester, prev_semester = _get_semesters()

    semesters = [current_semester, prev_semester]

    lecturer_blacklist = [_id(name) for name in config['courses']['blacklist']]
    lecturers = [p for p in people if p['identifier'] not in lecturer_blacklist]

    for semester in semesters:
        print(f'Fetching courses for semester {semester}')

        courses = load_courses(lecturers, semester=semester)
        parsed_courses = parse_courses(courses, lecturers)

        with open(f'{DATA_DIR}/teaching/courses/{semester}.json', 'w+', encoding='utf-8') as f:
            f.write(json.dumps(parsed_courses, indent=4))

    # fetch publications
    publisher_blacklist = [_id(name) for name in config['publications']['blacklist']]
    publishers = [p for p in people if p['identifier'] not in publisher_blacklist]

    print('Loading BibTeX records')
    bibtex = load_bibtex(publishers)

    print('Parsing BibTeX entries')
    bib_db = parse_bibtex(bibtex)

    print('Fetching publications')
    publications = load_publications(publishers, session=s)
    with open(f'{DATA_DIR}/publications.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(publications, indent=4))

    print('Parsing publications')
    name_map = {}
    for entry in config['publications']['transform']:
        to = entry['to']
        for fr in entry['from']:
            name_map[fr] = to

    posts = parse_publications(publications, bib_db, name_map)

    print(f'Storing results to "{PUBLICATION_DIR}". Skipping existing records.')
    save_publications(posts, bib_db, PUBLICATION_DIR)


if __name__ == '__main__':
    main()
