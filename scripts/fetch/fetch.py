import argparse
import json
import os
import re
from os.path import basename, normpath

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

TISS_BASE = 'https://tiss.tuwien.ac.at'
PUBLIK_BASE = 'https://publik.tuwien.ac.at'
PEOPLE_URL = f'{TISS_BASE}/api/orgunit/v22/id/{BIG_TID}?persons=true'
PERSON_DETAIL_URL = TISS_BASE + '/api/person/v22/id/{}'
COURSE_URL = TISS_BASE + '/api/course/lecturer/{}'
PUBLICATION_URL = f'{PUBLIK_BASE}/pubexport.php'
BIBTEX_URL = f'{PUBLIK_BASE}/pubbibtex.php'


def _id(name):
    # might need adjustments in the future, if people with non standard chars in their names join BIG
    # and those chars are unwanted in the url.
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
    if term == 'W':
        term = 'S'
    else:
        term = 'W'
        year -= 1

    prev = f'{year}{term}'

    return current, prev


def load_courses(lecturers, semester=None, session=requests.Session()):
    def oids_to_author_ids(oids):
        if type(oids) == str:
            oids = [oids]
        res = []
        for oid in oids:
            ps = [p['identifier'] for p in lecturers if oid == str(p['oid'])]
            res.extend(ps)
        return res

    course_dict = {}

    namespaces = {
      f'{TISS_BASE}/api/schemas/course/v10': None,
      f'{TISS_BASE}/api/schemas/hasCourse/v10': None,
      f'{TISS_BASE}/api/schemas/i18n/v10': None
    }

    for lect in lecturers:
        url = COURSE_URL.format(lect['oid'])
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

    courses = list(course_dict.values())

    lecture_exercise_course_types = ['VO', 'VU']
    seminar_project_course_types = ['SE', 'PV', 'PR']

    lectures_exercises = [c for c in courses if c['courseType'] in lecture_exercise_course_types]
    seminars_projects = [c for c in courses if c['courseType'] in seminar_project_course_types]
    other = [c for c in courses if c['courseType'] not in
             (lecture_exercise_course_types + seminar_project_course_types)]

    result = {}

    for identifier, courses in [('lectures_exercises', lectures_exercises),
                                ('seminars_projects', seminars_projects),
                                ('other', other)]:
        result[identifier] = [{
            'authors': sorted(oids_to_author_ids(course['lecturers']['oid'])),
            'number': course["courseNumber"],
            'url': course["url"],
            'type': course["courseType"],
            'title': course["title"]["en"]
        } for course in courses]

    return result


def load_publications(researchers, bib_db, author_transform_map, session=requests.Session()):
    # this map is used to map the given type of a pub record (key) to the respective element for further information
    type_map = {
        'Herausgabe eines Bandes einer Buchreihe': 'herausgabe_buchreihe',
        'Zeitschriftenartikel': 'zeitschriftenartikel',
        'Buchbeitrag': 'buchbeitrag',
        'Beitrag in Tagungsband': 'beitrag_tagungsband',
        'Vortrag mit Tagungsband': 'vortrag_poster_mit_tagungsband',
        'Vortrag ohne Tagungsband': 'vortrag_poster_ohne_tagungsband',
        'Patent (Erstanmeldung)': 'patent',
        'Habilitationsschrift': 'habilitation',
        'Dissertation': 'diss_dipl',
        'Diplom- oder Master-Arbeit': 'diss_dipl',
        'Wissenschaftlicher Bericht': 'bericht',
        'Architektur- und Städtebauentwurf': 'architektur_staedtebauentwurf',
        'Rezension in Fach- oder überregionaler Zeitschrift': 'rezension',
        'Teilnahme an Ausstellung mit Katalog': 'ausstellung_mit_katalog',
        'Teilnahme an Ausstellung ohne Katalog': 'ausstellung_ohne_katalog',
        'Nichttextl. wiss. Veröffentlichung (gem. Wissensbilanz-VO)': 'nichttextl_veroeffentlichung',
        'Editorial in wiss. Zeitschrift': 'editorial_zeitschrift',
        'Editorial in CD- oder Web-Tagungsband': 'editorial_beitrag_cd_tagungsband',
        'Buch-Herausgabe': 'buch_herausgabe',
        'Monographie (Erstauflage)': 'buch',
        'Monographie (Folgeauflage)': 'buch',
        'Beitrag in elektron. Zeitschrift': 'elektron_zeitschrift',
        'Vortrag mit CD- oder Web-Tagungsband': 'vortrag_poster_mit_cd_tagungsband',
        'Beitrag in CD- oder Web-Tagungsband': 'beitrag_cd_tagungsband',
        'Haupt-(Keynote-)Vortrag mit Tagungsband': 'vortrag_poster_mit_tagungsband',
        'Haupt-(Keynote-)Vortrag ohne Tagungsband': 'vortrag_poster_ohne_tagungsband',
        'Posterpräsentation mit Tagungsband': 'vortrag_poster_mit_tagungsband',
        'Posterpräsentation ohne Tagungsband': 'vortrag_poster_ohne_tagungsband',
        'Posterpräsentation mit CD- oder Web-Tagungsband': 'vortrag_poster_mit_cd_tagungsband',
    }

    # mappings of bibtex type to adacemic framework type
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

    publications = []
    posts = []

    for res in researchers:
        # func: 1 -> only fetch publications where the person is actually an author (skip supervisions etc.)
        query = {'zuname': res['last_name'], 'vorname': res['first_name'],
                 'inst': 'E194', 'abt': '03', 'func': '1', 'lang': '2'}
        r = session.get(PUBLICATION_URL, params=query)
        content = r.content.decode('ISO-8859-1')
        xml = xmltodict.parse(content, encoding='utf-8')['export']  # get root element
        if 'publikation' not in xml:
            continue
        result = xml['publikation'] if type(xml['publikation']) == list else [xml['publikation']]
        publications.extend(result)

    for pub in publications:
        pub_id = pub['pub_id'].lower()
        pub_type = pub['type']

        if pub_type in type_map:
            pub_type = type_map[pub_type]
        else:
            # if this error occurs, there is not mapping for the given pub_type in the dicts above.
            print(f'Skipping publication "{pub_id}" due to unknown pub-type: {pub_type}.')
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
        publik_link = pub['infolink']

        year = '2000'
        month = '01'
        day = '01'
        # getting the correct date is type specific and cannot be done the same way for all publications
        if 'datum_von' in pub[pub_type]:
            dateparts = pub[pub_type]['datum_von'].split('-')
            if len(dateparts) >= 3:
                month, day, year = dateparts[0], dateparts[1], dateparts[2]
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

        # type specific content
        reference_search = re.search(r';(.*?)<br><br>', pub['reference'])
        extra = None
        if reference_search:
            extra = reference_search.group(1)
            # remove html and normalize whitespace
            extra = re.sub(r' {2,}', ' ', re.sub('<[^<]+?>', '', extra).strip().rstrip('.'))

        # create the post
        post = frontmatter.Post(content='', title=title, authors=authors, date=f'{year}-{month}-{day}',
                                publishDate=f'{year}-{month}-{day}', publication_types=[str(academic_type)],
                                abstract=abstract, featured=False, url_pdf=pdf_link, publication=extra,
                                links=[{'name': 'Publik', 'url': publik_link}])

        posts.append((pub_id, post))

    return publications, posts


def load_bibtex(publishers, session=requests.Session()):
    bibtex = ''

    for pub in publishers:
        query = {'zuname': pub['last_name'], 'vorname': pub['first_name'], 'inst': 'E194', 'abt': '03', 'func': '1'}
        r = session.get(BIBTEX_URL, params=query)
        result = r.content.decode('ISO-8859-1')
        for line in result.split(os.linesep):
            if len(line) == 0 or line.startswith('BibTeX-Export:') or \
              line.endswith('ausgegeben') or line.startswith('@comment'):
                continue
            bibtex += line + '\n'
        bibtex += '\n'

    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.customization = bibtexparser.customization.convert_to_unicode
    parser.ignore_nonstandard_types = False
    bib_database = bibtexparser.loads(bibtex_str=bibtex, parser=parser)

    return bib_database


def main():
    argparser = argparse.ArgumentParser(description='BIG data fetch script.')
    argparser.add_argument('-m', '--members',
                           help='fetch member data of the BIG organization in TISS', action='store_true',
                           dest='fetch_members')
    argparser.add_argument('-c', '--courses',
                           help='fetch courses of current and previous semester', action='store_true',
                           dest='fetch_courses')
    argparser.add_argument('-p', '--publications',
                           help='fetch publications affiliated with BIG members', action='store_true',
                           dest='fetch_publications')
    argparser.add_argument('-o', '--override',
                           help='override existing content', action='store_true',
                           dest='override')
    argparser.add_argument('-C', '--config',
                           help='provide the path of the config file. Defaults to "config.yml"',
                           default='config.yml',
                           metavar='PATH', dest='config_path')
    argparser.add_argument('-g' '--groups',
                           help='provide the path of the group config file. Defaults to "groups.yml"',
                           default='groups.yml',
                           metavar='PATH', dest='group_config_path')
    argparser.add_argument('-b', '--base',
                           help='provide the project base dir. Defaults to "../.."',
                           default='../..',
                           metavar='PATH', dest='base_path')
    argparser.add_argument('-d', '--debug',
                           help='dumps fetched data to the /data directory', action='store_true',
                           dest='debug')
    args = argparser.parse_args()

    if not (args.fetch_members or args.fetch_courses or args.fetch_publications):
        print('Aborting as there is nothing to do. Run with "-h" for help.')
        return

    if not args.override:
        print('Override is disabled. Existing files will not be touched. Run with "-o" to enable override.')

    base_dir = args.base_path.rstrip('/')
    data_dir = base_dir + '/data'
    content_dir = base_dir + '/content'
    people_dir = content_dir + '/people'
    publication_dir = content_dir + '/publication'

    template_dir = 'templates'

    # load config
    try:
        with open(args.config_path, 'r', encoding='utf-8') as yml:
            config = yaml.safe_load(yml)
    except Exception as e:
        print('Cannot read config file: ', e)
        return

    # load group config
    try:
        with open(args.group_config_path, 'r', encoding='utf-8') as yml:
            group_config = yaml.safe_load(yml)
    except Exception as e:
        print('Cannot read group config file: ', e)
        return

    s = requests.Session()

    # fetch members
    r = s.get(PEOPLE_URL)
    data = r.json()
    tiss_employees = data['employees']

    # add identifiers
    for person in tiss_employees:
        person['identifier'] = _id(person['first_name'] + ' ' + person['last_name'])

    # apply whitelist
    print('Applying whitelist based on group config.')

    groups = group_config['groups']
    name_grouped_people = {}
    for group_name, group_members in groups.items():
        for name in group_members:
            if name not in name_grouped_people:
                name_grouped_people[name] = group_name
    id_grouped_people = dict((_id(k), v) for k, v in name_grouped_people.items())

    tiss_employees = [p for p in tiss_employees if p['identifier'] in id_grouped_people.keys()]

    if args.fetch_members:
        print('Fetching people. Creating files for new people in the "content/authors" directory.')

        # apply data from TISS to profiles (and create new pages)
        # only profiles listed in the group config will be handled
        for person in tiss_employees:
            first_name = person['first_name']
            last_name = person['last_name']
            name = f'{first_name} {last_name}'
            directory = f'{people_dir}/{person["identifier"]}'
            template_source = template_dir + '/authors/user/_index.md'

            # create folder
            if not os.path.exists(directory):
                # dir does not exist
                print(f'Creating author files for {name}.')
                os.makedirs(directory)
            elif not args.override:
                # dir does exist, but override is disabled
                continue
            else:
                # dir does exist
                template_source = directory + '/_index.md'

            # download profile pic or copy default
            pic_dest = directory + '/avatar.jpg'
            if person['picture_uri']:
                urllib.request.urlretrieve(TISS_BASE + person['picture_uri'], pic_dest)
            else:
                shutil.copyfile(template_dir + '/authors/user/avatar.jpg', pic_dest)

            # apply metadata to markdown front matter
            post = frontmatter.load(template_source)

            pairs = []
            if 'pairs' in post:
                pairs = post['pairs']

            email = person["main_email"]
            big_mails = list(filter(lambda mail: '@big.tuwien.ac.at' in mail, person['other_emails']))
            if len(big_mails) > 0:
                email = big_mails[0]

            mail_pair = {'key': 'Mail', 'value': email, 'link': f'mailto:{email}'}

            phone = person['main_phone_number']
            phone_pair = None
            if phone:
                phone_pair = {'key': 'Phone', 'value': phone, 'link': f'tel:{phone}'}

            room_pair = None
            if 'room_code' in person:
                room = person['room_code']
                room_pair = {'key': 'Location', 'value': room}

            # get remaining pairs that might have been defined individually such as office hours
            remaining_pairs = list(filter(
                lambda p: 'key' not in p or (p['key'] != 'Mail' and p['key'] != 'Phone' and p['key'] != 'Location'),
                pairs
            ))

            pairs = [mail_pair]
            if phone_pair:
                pairs.append(phone_pair)
            if room_pair:
                pairs.append(room_pair)
            pairs.extend(remaining_pairs)

            post['name'] = name
            post['email'] = email
            post['authors'] = [person["identifier"]]
            post['role'] = person['preceding_titles']
            post['pairs'] = pairs

            with open(f'{directory}/_index.md', 'w+', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))

        # adjust groups for all profiles
        default_group = group_config['default']
        existing_profiles = [f.path for f in os.scandir(people_dir) if f.is_dir()]
        for profile_path in existing_profiles:
            folder_id = basename(normpath(profile_path))
            group = id_grouped_people.get(folder_id, default_group)

            index_file = profile_path + '/_index.md'
            post = frontmatter.load(index_file)
            post['user_groups'] = [group]
            with open(index_file, 'w+', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))

        if args.debug:
            with open(f'{data_dir}/people.json', 'w+', encoding='utf-8') as f:
                f.write(json.dumps(tiss_employees, indent=4))

    if args.fetch_courses:
        # fetch courses. has to be done separately for each person
        # as fetching courses for the institute returns an empty set
        print('Fetching courses. Creating files for courses in the "content/teaching" directory.')

        current_semester, prev_semester = _get_semesters()

        semesters = [current_semester, prev_semester]

        lecturer_blacklist = [_id(name) for name in config['courses']['blacklist']]
        lecturers = [p for p in tiss_employees if p['identifier'] not in lecturer_blacklist]

        for semester in semesters:
            print(f'Fetching courses for semester {semester}.')

            courses = load_courses(lecturers, semester=semester, session=s)

            with open(f'{data_dir}/teaching/courses/{semester}.json', 'w+', encoding='utf-8') as f:
                f.write(json.dumps(courses, indent=4))

    if args.fetch_publications:
        # fetch publications

        # right now publications are fetched based on the people records in TISS. If there is no TISS record
        # in the BIG org unit for this person, no publications will be loaded.
        # If required, this step can be skipped by splitting the names from the config into first and last name.
        # (edge case: people with multiple first names)

        publisher_blacklist = [_id(name) for name in config['publications']['blacklist']]
        publishers = [p for p in tiss_employees if p['identifier'] not in publisher_blacklist]

        print('Fetching BibTeX records.')
        bib_db = load_bibtex(publishers, session=s)

        print('Fetching publications.')
        publications, posts = load_publications(publishers, bib_db, config['publications']['transform'], session=s)

        if args.debug:
            with open(f'{data_dir}/publications.json', 'w+', encoding='utf-8') as f:
                f.write(json.dumps(publications, indent=4))

        print('Storing results to "content/publication".')
        for identifier, post in posts:
            directory = f'{publication_dir}/{identifier}'

            # create folder
            if not os.path.exists(directory):
                os.makedirs(directory)
            elif not args.override:
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


if __name__ == '__main__':
    main()
