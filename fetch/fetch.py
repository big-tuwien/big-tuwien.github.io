import codecs
import json
import os
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

CI_TEMPLATE_DIR = 'templates'

DATA_DIR = '../data'
CONTENT_DIR = '../content'
PEOPLE_DIR = CONTENT_DIR + '/authors'
TEACHING_DIR = CONTENT_DIR + '/teaching'

TISS_BASE = 'https://tiss.tuwien.ac.at'
PEOPLE_URL = f'{TISS_BASE}/api/orgunit/v22/id/{BIG_TID}?persons=true'
PROJECTS_ONGOING_URL = f'{TISS_BASE}/api/pdb/rest/projectsearch/v2?instituteOid={BIG_OID}&status=1'
PROJECTS_FINISHED_URL = f'{TISS_BASE}/api/pdb/rest/projectsearch/v2?instituteOid={BIG_OID}&status=2'
COURSE_LECTURER_URL = TISS_BASE + '/api/course/lecturer/{}'

COURSE_NAMESPACE_CONFIG = {
    f'{TISS_BASE}/api/schemas/course/v10': None,
    f'{TISS_BASE}/api/schemas/hasCourse/v10': None,
    f'{TISS_BASE}/api/schemas/i18n/v10': None
}


def _id(first_name, last_name):
    return (first_name[0] + last_name).lower().replace('ö', 'oe').replace('ä', 'ae').replace('ü', 'ue')\
            .replace('ß', 'sz').replace(' ', '').replace('-', '')


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


def _course_table(courses, people):
    content = '| No. | Course Title German | Course Title English | Lecturers |\n' \
              '|-----|---------------------|----------------------|-----------|\n'
    for course in courses:
        authors = ['{{% mention "' + p['short_name'] + '" %}}' for p in people if str(p['oid']) in course['lecturers']['oid']]
        author_string = ', '.join(authors)
        content += f'| [{course["courseNumber"]}]({course["url"]}) | {course["title"]["de"]} ' \
                   f'| {course["title"]["en"]} ' \
                   '| ' + author_string + ' |\n'

    return content


def _create_course_post(courses, people, semester, template_path):
    post = frontmatter.load(template_path)
    post['linktitle'] = semester
    post['date'] = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()

    lectures_exercises = [c for c in courses if c['courseType'] in LECTURE_EXERCISE_COURSE_TYPES]
    seminars_projects = [c for c in courses if c['courseType'] in SEMINAR_PROJECT_COURSE_TYPES]
    other = [c for c in courses if c['courseType'] not in (LECTURE_EXERCISE_COURSE_TYPES + SEMINAR_PROJECT_COURSE_TYPES)]

    content = '## Lectures and Exercises\n\n' \
              f'{_course_table(lectures_exercises, people)}\n' \
              '## Seminars and Projects\n\n' \
              f'{_course_table(seminars_projects, people)}\n'

    # only display 'other' section if not empty
    if other:
        content += '## Other\n\n' \
                   f'{_course_table(other, people)}\n'

    post.content = content
    return post


def get_lecturer_courses(lecturer_oids, semester=None, session=requests.Session()):
    course_dict = {}

    for oid in lecturer_oids:
        url = COURSE_LECTURER_URL.format(oid)
        query = {}
        if session:
            query['semester'] = semester
        r = session.get(url, params=query)
        xml_dict = xmltodict.parse(
          r.content, encoding='utf-8', process_namespaces=True,
          namespaces=COURSE_NAMESPACE_CONFIG
        )

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


def main():
    # load config
    with open('config.yml', 'r') as f:
        try:
            config = yaml.safe_load(f)
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
        person['short_name'] = _id(person['first_name'], person['last_name'])

    # apply whitelist
    print('Applying people whitelist')
    people = [p for p in people if p['short_name'] in config['people']['whitelist']]

    for person in people:
        first_name = person['first_name']
        last_name = person['last_name']
        name = f'{first_name} {last_name}'
        directory = f'{PEOPLE_DIR}/{person["short_name"]}'

        # create folder
        if not os.path.exists(directory):
            print(f'Creating author files for {name}')
            os.makedirs(directory)
        else:
            print(f'Skipping {name} ({person["short_name"]}) - profile already exists')
            continue

        # download profile pic or copy default
        pic_dest = directory + '/avatar.jpg'
        if person['picture_uri']:
            urllib.request.urlretrieve(TISS_BASE + person['picture_uri'], pic_dest)
        else:
            shutil.copyfile(CI_TEMPLATE_DIR + '/authors/user/avatar.jpg', pic_dest)

        # apply metadata to markdown front matter
        post = frontmatter.load(CI_TEMPLATE_DIR + '/authors/user/_index.md')
        post['name'] = name
        post['authors'] = [person["short_name"]]
        post['role'] = person['preceding_titles']
        post['email'] = person['main_email']
        social = [{'icon': 'envelope', 'icon_pack': 'fas', 'link': f'mailto:{person["main_email"]}'}]
        if person['main_phone_number']:
            social.append({'icon': 'phone', 'icon_pack': 'fas', 'link': f'tel:{person["main_phone_number"]}'})
        post['social'] = social
        with codecs.open(f'{directory}/_index.md', 'w+', 'utf-8') as f:
            f.write(frontmatter.dumps(post))

    with codecs.open(f'{DATA_DIR}/people.json', 'w+', 'utf-8') as f:
        f.write(json.dumps(people, indent=4))

    # fetch courses. has to be done separately for each person (fetching courses for the institute returns an empty set)
    print('Fetching courses. Creating files for courses in the "content/teaching" directory')

    current_semester, prev_semester = _get_semesters()

    semesters = [(current_semester, '_index.md'), (prev_semester, 'prev.md')]

    for semester, file in semesters:
        print(f'Fetching courses for semester {semester} -> {file}')

        lecturer_oids = [p['oid'] for p in people]
        courses = get_lecturer_courses(lecturer_oids, semester=semester)

        # apply metadata to markdown front matter
        post = _create_course_post(courses, people, semester, f'{CI_TEMPLATE_DIR}/teaching/{file}')

        with codecs.open(f'{TEACHING_DIR}/{file}', 'w+', 'utf-8') as f:
            f.write(frontmatter.dumps(post))

        with codecs.open(f'{DATA_DIR}/courses_{semester}.json', 'w+', 'utf-8') as f:
            f.write(json.dumps(courses, indent=4))


if __name__ == '__main__':
    main()
