import os
import shutil
import urllib.request

import frontmatter
import html2markdown
import requests
from bs4 import BeautifulSoup


def _id(name):
    return name.lower().replace(' ', '-').replace('ö', 'oe').replace('ä', 'ae').replace('ü', 'ue') \
           .replace('ß', 'sz').replace(' ', '')


def migrate_big_profile(profile_url, create=True, picture=True):
    r = s.get(profile_url)
    raw_html = r.content.decode()
    soup = BeautifulSoup(raw_html, 'html.parser')

    title = soup.select('#person-title')[0].string
    title = str(title) if title else None
    name = str(soup.select('#person-name')[0].string)
    name = str(name) if name else None
    identifier = _id(name)

    email = soup.select('#email .general-info-text')
    email = str(email[0].string) if len(email) > 0 else None
    telephone = soup.select('#telephone .general-info-text')
    telephone = str(telephone[0].string) if len(telephone) > 0 else None
    location = soup.select('#location .general-info-text')
    location = str(location[0].string) if len(location) > 0 else None
    office_hours = soup.select('#office-hours .general-info-text')
    office_hours = str(office_hours[0].string) if len(office_hours) > 0 else None
    content_html = soup.select('#profile')
    content_html = str(content_html[0]) if len(content_html) > 0 else ''
    content_html = content_html.replace('<div id="profile">', '').replace('<h3>Profile</h3>', '').replace('</div>', '')
    content_markdown = html2markdown.convert(content_html).replace('&nbsp;', '')
    picture_uri = soup.select('#person-image')
    picture_uri = picture_uri[0]['src'] if len(picture_uri) > 0 else None

    # create folder
    directory = f'{PEOPLE_DIR}/{identifier}'
    template_source = TEMPLATE_DIR + '/authors/user/_index.md'

    if not os.path.exists(directory):
        if not create:
            return
        print(f'Creating author files for {name}')
        os.makedirs(directory)
    else:
        template_source = directory + '/_index.md'

    if picture:
        # download profile pic or copy default
        pic_dest = directory + '/avatar.jpg'
        if picture_uri:
            urllib.request.urlretrieve(picture_uri, pic_dest)
        else:
            shutil.copyfile(TEMPLATE_DIR + '/authors/user/avatar.jpg', pic_dest)

    # apply metadata to markdown front matter
    post = frontmatter.load(template_source)
    post['name'] = name
    post['authors'] = [identifier]
    post['role'] = title
    post['email'] = email
    pairs = []
    if email:
        pairs.append({'key': 'Mail', 'value': email, 'link': f'mailto:{email}'})
    if telephone:
        pairs.append({'key': 'Phone', 'value': telephone, 'link': f'tel:{telephone}'})
    if location:
        pairs.append({'key': 'Location', 'value': location})
    if office_hours:
        pairs.append({'key': 'Office hours', 'value': office_hours})
    post['pairs'] = pairs

    post.content = content_markdown

    with open(f'{directory}/_index.md', 'w+', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))


TEMPLATE_DIR = 'templates'
CONTENT_DIR = '../content'
PEOPLE_DIR = CONTENT_DIR + '/people'

BIG_BASE = 'https://big.tuwien.ac.at'

s = requests.Session()

# migrate people at big
PPL_URL = f'{BIG_BASE}/people/'

ppl_r = s.get(PPL_URL)
ppl_raw_html = ppl_r.content.decode()
ppl_soup = BeautifulSoup(ppl_raw_html, 'html.parser')
profile_refs = ppl_soup.select('#main a')
profile_refs = [a for a in profile_refs if a['href'].startswith('/people') and not 'visitors-and-friends' in a['href']]

for ref in profile_refs:
    url = f'{BIG_BASE}{ref["href"]}'
    if BIG_BASE not in url:
        print(url)
        continue
    migrate_big_profile(url, picture=False)

# migrate visitors and friends
VAF_URL = f'{BIG_BASE}/people/visitors-and-friends/'

vaf_r = s.get(VAF_URL)
vaf_raw_html = vaf_r.content.decode()
vaf_soup = BeautifulSoup(vaf_raw_html, 'html.parser')
profile_refs = vaf_soup.select('#main a')

for ref in profile_refs:
    url = ref["href"] if ref["href"].startswith('http') else f'{BIG_BASE}{ref["href"]}'
    if BIG_BASE not in url:
        print(url)
        continue
    migrate_big_profile(url)


