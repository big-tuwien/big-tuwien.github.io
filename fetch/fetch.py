import codecs
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


def main():
    # load config
    with open('config.yml', 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print('Cannot read config.yml: ', e)
            return

    s = requests.Session()

    # handle people
    r = s.get(PEOPLE_URL)
    data = r.json()
    people = data['employees']

    print('Fetching people. Creating files for people with no own folder in the "content/authors" directory')

    for person in people:
        first_name = person['first_name']
        last_name = person['last_name']
        name = f'{first_name} {last_name}'
        identifier = (first_name[0] + last_name).lower().replace('ö', 'oe').replace('ä', 'ae').replace('ü', 'ue')\
            .replace('ß', 'sz').replace(' ', '').replace('-', '')
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

    # fetch courses for each person (fetching courses for the institute returns an empty set)
    for person in people:
        url = COURSE_LECTURER_URL.format(person['oid'])
        r = s.get(url)
        parse_res = xmltodict.parse(
            r.content, encoding='utf-8', process_namespaces=True,
            namespaces=COURSE_NAMESPACE_CONFIG
        )['tuvienna']

        if 'course' not in parse_res:
            continue
        courses = parse_res['course']


if __name__ == '__main__':
    main()
