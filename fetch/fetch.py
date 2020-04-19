import codecs
import json
import os
import requests
import frontmatter
import urllib.request
import shutil
import yaml
import xmltodict

BIG_TID = 4760
BIG_OID = 18460477

CI_TEMPLATE_DIR = 'templates'

DATA_DIR = '../data'
CONTENT_DIR = '../content'
PEOPLE_DIR = CONTENT_DIR + '/authors'

PEOPLE_URL = f'https://tiss.tuwien.ac.at/api/orgunit/v22/id/{BIG_TID}?persons=true'
PROJECTS_ONGOING_URL = f'https://tiss.tuwien.ac.at/api/pdb/rest/projectsearch/v2?instituteOid={BIG_OID}&status=1'
PROJECTS_FINISHED_URL = f'https://tiss.tuwien.ac.at/api/pdb/rest/projectsearch/v2?instituteOid={BIG_OID}&status=2'
COURSE_LECTURER_URL = 'https://tiss.tuwien.ac.at/api/course/lecturer/{}'

COURSE_NAMESPACE_CONFIG = {
    'https://tiss.tuwien.ac.at/api/schemas/course/v10': None,
    'https://tiss.tuwien.ac.at/api/schemas/hasCourse/v10': None,
    'https://tiss.tuwien.ac.at/api/schemas/i18n/v10': None
}


def _id(first_name, last_name):
    return (first_name[0] + last_name).lower().replace('ö', 'oe').replace('ä', 'ae').replace('ü', 'ue')\
            .replace('ß', 'sz').replace(' ', '').replace('-', '')


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

    # apply whitelist
    print('Applying people whitelist')
    people = list(filter(lambda p: _id(p['first_name'], p['last_name']) in config['people']['whitelist'], people))

    for person in people:
        first_name = person['first_name']
        last_name = person['last_name']
        name = f'{first_name} {last_name}'
        identifier = _id(first_name, last_name)
        directory = f'{PEOPLE_DIR}/{identifier}'

        if identifier not in config['people']['whitelist']:
            print(f'Skipping {name} ({identifier}) - person not whitelisted')
            continue

        # create folder
        if not os.path.exists(directory):
            print(f'Creating author files for {name}')
            os.makedirs(directory)
        else:
            print(f'Skipping {name} ({identifier}) - profile already exists')
            continue

        # download profile pic or copy default
        pic_dest = directory + '/avatar.jpg'
        if person['picture_uri']:
            urllib.request.urlretrieve('https://tiss.tuwien.ac.at' + person['picture_uri'], pic_dest)
        else:
            shutil.copyfile(CI_TEMPLATE_DIR + '/authors/user/avatar.jpg', pic_dest)

        # apply metadata to markdown front matter
        post = frontmatter.load(CI_TEMPLATE_DIR + '/authors/user/_index.md')
        post['name'] = name
        post['authors'] = [identifier]
        post['role'] = person['function']
        post['email'] = person['main_email']
        social = [{'icon': 'envelope', 'icon_pack': 'fas', 'link': f'mailto:{person["main_email"]}'}]
        if person['main_phone_number']:
            social.append({'icon': 'phone', 'icon_pack': 'fas', 'link': f'tel:{person["main_phone_number"]}'})
        post['social'] = social
        with codecs.open(f'{directory}/_index.md', 'w+', 'utf-8') as f:
            f.write(frontmatter.dumps(post))

    with open(DATA_DIR + '/people.json', 'w+') as f:
        f.write(json.dumps(people, indent=4))

    # fetch courses. has to be done separately for each person (fetching courses for the institute returns an empty set)
    courses = {}

    print('Fetching courses. Creating files for new courses in the "content/teaching" directory')

    for person in people:
        url = COURSE_LECTURER_URL.format(person['oid'])
        r = s.get(url)
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
            if course_id in courses:
                continue
            courses[course_id] = course

    with open(DATA_DIR + '/courses.json', 'w+') as f:
        f.write(json.dumps(list(courses.values()), indent=4))


if __name__ == '__main__':
    main()
