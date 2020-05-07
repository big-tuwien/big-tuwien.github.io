import os
import shutil
import urllib

import frontmatter
import html2markdown
import requests
from bs4 import BeautifulSoup


def _id(name):
    return name.lower().replace(' ', '-').replace('ö', 'oe').replace('ä', 'ae').replace('ü', 'ue') \
           .replace('ß', 'sz').replace(' ', '')


TEMPLATE_DIR = 'templates'
CONTENT_DIR = '../content'
PEOPLE_DIR = CONTENT_DIR + '/people'

BIG_BASE = 'https://big.tuwien.ac.at'

# migrate visitors and friends
VAF_URL = f'{BIG_BASE}/people/visitors-and-friends/'

s = requests.Session()
vaf_r = s.get(VAF_URL)
vaf_raw_html = vaf_r.content.decode()
vaf_soup = BeautifulSoup(vaf_raw_html, 'html.parser')
profile_refs = vaf_soup.select('#main a')

for ref in profile_refs:
    profile_url = ref["href"] if ref["href"].startswith('http') else f'{BIG_BASE}{ref["href"]}'
    if BIG_BASE not in profile_url:
        print(profile_url)
        continue

    r = s.get(profile_url)
    raw_html = r.content.decode()
    soup = BeautifulSoup(raw_html, 'html.parser')

    title = soup.select('#person-title')[0].string
    name = soup.select('#person-name')[0].string
    identifier = _id(name)

    email = soup.select('#email .general-info-text')
    email = email[0].string if len(email) > 0 else None
    telephone = soup.select('#telephone .general-info-text')
    telephone = telephone[0].string if len(telephone) > 0 else None
    location = soup.select('#location .general-info-text')
    location = location[0].string if len(location) > 0 else None
    office_hours = soup.select('#office-hours .general-info-text')
    office_hours = office_hours[0].string if len(office_hours) > 0 else None
    content_html = soup.select('#profile')
    content_html = str(content_html[0]) if len(content_html) > 0 else ''
    content_html = content_html.replace('<div id="profile">', '').replace('<h3>Profile</h3>', '').replace('</div>', '')
    content_markdown = html2markdown.convert(content_html).replace('&nbsp;', '')

    # create folder
    directory = f'{PEOPLE_DIR}/{identifier}'

    if not os.path.exists(directory):
        print(f'Creating author files for {name}')
        os.makedirs(directory)
    else:
        print(f'Skipping {name} ({identifier}) - profile already exists')
        continue

    # download profile pic or copy default
    # pic_dest = directory + '/avatar.jpg'
    # if person['picture_uri']:
    #     urllib.request.urlretrieve(TISS_BASE + person['picture_uri'], pic_dest)
    # else:
    #     shutil.copyfile(TEMPLATE_DIR + '/authors/user/avatar.jpg', pic_dest)

    # apply metadata to markdown front matter
    post = frontmatter.load(TEMPLATE_DIR + '/authors/user/_index.md')
    post['name'] = name
    post['authors'] = [identifier]
    post['role'] = title
    post['email'] = email
    pairs = []
    if email:
        pairs.append({'key': 'Mail', 'value': email, 'link': f'mailto:{email}'})
    if telephone:
        pairs.append({'key': 'Phone', 'value': telephone, 'link': f'tel:{telephone}'})
    post['pairs'] = pairs

    with open(f'{directory}/_index.md', 'w+', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
