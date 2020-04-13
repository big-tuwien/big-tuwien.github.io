import codecs
import os
import requests
import frontmatter
import urllib.request
import shutil
import yaml

CI_TEMPLATE_DIR = 'templates'
CONTENT_DIR = '../content'
PEOPLE_DIR = CONTENT_DIR + '/authors'

PEOPLE_URL = 'https://tiss.tuwien.ac.at/api/orgunit/v22/id/4760?persons=true'

with open('config.yml', 'r') as f:
    try:
        config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print('Cannot read config.yml')
        print(e)

s = requests.Session()

r = s.get(PEOPLE_URL)
data = r.json()
people = data['employees']

print('Fetching people. Creating files for people with no own folder in the "content/authors" directory')

for person in people:
    first_name = person['first_name']
    last_name = person['last_name']
    name = f'{first_name} {last_name}'
    short_name = (first_name[0] + last_name).lower()
    identifier = short_name.replace('ö', 'oe').replace('ä', 'ae').replace('ü', 'ue')\
        .replace('ß', 'sz').replace(' ', '').replace('-', '')
    directory = f'{PEOPLE_DIR}/{identifier}'

    if short_name not in config['people']['whitelist']:
        print(f'Skipping {name} ({short_name}) - not whitelisted')
        continue

    # create folder
    if not os.path.exists(directory):
        print(f'Creating author files for {name}')
        os.makedirs(directory)
    else:
        print(f'Skipping {name} ({short_name}) - already exists')
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
    post['tel'] = person['main_phone_number']
    with codecs.open(f'{directory}/_index.md', 'w+', 'utf-8') as f:
        f.write(frontmatter.dumps(post))
