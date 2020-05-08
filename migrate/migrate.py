import os
import shutil
import urllib.request
from datetime import datetime

import frontmatter
import html2markdown
import pytz
import requests
from bs4 import BeautifulSoup


def _id(name):
    if name == 'Gerti Kappel':
        return 'gertrude-kappel'
    return name.lower().replace(' ', '-').replace('ö', 'oe').replace('ä', 'ae').replace('ü', 'ue') \
           .replace('ß', 'sz').replace(' ', '')


def _title(title):
    # hyphenize title, remove non ascii chars and convert to lower
    title = title.lower().replace(':', '').replace('?', '').replace(' - ', '-').replace(' – ', '-')\
        .replace('(', '').replace(')', '').replace('@', ' ').replace('.', '-').replace(' & ', '-')\
        .strip().replace(' ', '-')
    return ''.join([i if ord(i) < 128 else '' for i in title])


def migrate_big_profile(profile_url, output_dir, create=True, picture=True):
    prof_r = s.get(profile_url)
    prof_raw_html = prof_r.content.decode()
    prof_soup = BeautifulSoup(prof_raw_html, 'html.parser')

    title = prof_soup.select('#person-title')[0].string
    title = str(title) if title else None
    name = str(prof_soup.select('#person-name')[0].string)
    name = str(name) if name else None
    identifier = _id(name)

    email = prof_soup.select('#email .general-info-text')
    email = str(email[0].string) if len(email) > 0 else None
    telephone = prof_soup.select('#telephone .general-info-text')
    telephone = str(telephone[0].string) if len(telephone) > 0 else None
    location = prof_soup.select('#location .general-info-text')
    location = str(location[0].string) if len(location) > 0 else None
    office_hours = prof_soup.select('#office-hours .general-info-text')
    office_hours = str(office_hours[0].string) if len(office_hours) > 0 else None
    content_html = prof_soup.select('#profile')
    content_html = str(content_html[0]) if len(content_html) > 0 else ''
    content_html = content_html.replace('<div id="profile">', '').replace('<h3>Profile</h3>', '').replace('</div>', '')
    content_markdown = html2markdown.convert(content_html).replace('&nbsp;', '')
    picture_uri = prof_soup.select('#person-image')
    picture_uri = picture_uri[0]['src'] if len(picture_uri) > 0 else None

    # create folder
    directory = f'{output_dir}/{identifier}'
    template_source = TEMPLATE_DIR + '/authors/user/_index.md'

    if not os.path.exists(directory):
        if not create:
            return
        print(f'Creating profile files for {name}')
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


def migrate_thesis(thesis_url, output_dir, ongoing, create=True):
    thes_r = s.get(thesis_url)
    thes_raw_html = thes_r.content.decode()
    thes_soup = BeautifulSoup(thes_raw_html, 'html.parser')
    base = thes_soup.select('#main')[0]

    title = str(base.find('h2').string)
    identifier = _title(title)
    kind = "Ongoing" if ongoing else "Finished"
    date = datetime.utcnow().replace(tzinfo=pytz.utc).isoformat(' ', 'seconds')
    ps = base.select('p')
    metadata = ps.pop(0)
    authors = metadata.find_all('em')
    authors = [str(a.string) for a in authors]
    supervisors = metadata.find_all('a')
    supervisors = [_id(str(sup.string)) for sup in supervisors]
    ps = [str(p) for p in ps]
    content_html = ''.join(ps).replace('<span class="markdown">', '').replace('</span>', '')
    content_markdown = html2markdown.convert(content_html)
    if len(supervisors) > 0:
        content_markdown += '\n\n' + '*Advised by ' + \
                            ', '.join(['{{% mention "' + sup + '" %}}' for sup in supervisors]) + \
                            '*'

    # create folder
    directory = f'{output_dir}/{identifier}'
    file = 'index.md'
    template_source = TEMPLATE_DIR + '/theses/thesis/index.md'

    if not os.path.exists(directory):
        if not create:
            return
        print(f'Creating thesis files for "{title}"')
        os.makedirs(directory)
    else:
        template_source = directory + '/' + file

    # apply metadata to markdown front matter
    post = frontmatter.load(template_source)
    post['title'] = title
    post['authors'] = authors
    post['tags'] = [kind]
    post['date'] = date

    post.content = content_markdown

    with open(f'{directory}/{file}', 'w+', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))


TEMPLATE_DIR = 'templates'
CONTENT_DIR = '../content'

BIG_BASE = 'https://big.tuwien.ac.at'

s = requests.Session()


def migrate_people():
    url = f'{BIG_BASE}/people/'
    output_dir = CONTENT_DIR + '/people'

    r = s.get(url)
    raw_html = r.content.decode()
    soup = BeautifulSoup(raw_html, 'html.parser')
    profile_refs = soup.select('#main a')
    profile_refs = [a for a in profile_refs if a['href'].startswith('/people') and not 'visitors-and-friends' in a['href']]

    for ref in profile_refs:
        url = f'{BIG_BASE}{ref["href"]}'
        if BIG_BASE not in url:
            print(url)
            continue
        migrate_big_profile(url, output_dir, picture=False)


def migrate_visitors_and_friends():
    url = f'{BIG_BASE}/people/visitors-and-friends/'
    output_dir = CONTENT_DIR + '/people'

    r = s.get(url)
    raw_html = r.content.decode()
    soup = BeautifulSoup(raw_html, 'html.parser')
    profile_refs = soup.select('#main a')

    for ref in profile_refs:
        url = ref["href"] if ref["href"].startswith('http') else f'{BIG_BASE}{ref["href"]}'
        if BIG_BASE not in url:
            print(url)
            continue
        migrate_big_profile(url, output_dir)


def migrate_master_theses():
    url = f'{BIG_BASE}/teaching/masters-theses/'
    output_dir = CONTENT_DIR + '/master-theses'

    r = s.get(url)
    raw_html = r.content.decode()
    soup = BeautifulSoup(raw_html, 'html.parser')
    ongoing_refs = soup.select('#main td[headers="thesisTitle ongoing"] a')
    finished_refs = soup.select('#main td[headers="thesisTitle finished"] a')

    for ref in ongoing_refs:
        url = ref["href"] if ref["href"].startswith('http') else f'{BIG_BASE}{ref["href"]}'
        migrate_thesis(url, output_dir, ongoing=True)

    for ref in finished_refs:
        url = ref["href"] if ref["href"].startswith('http') else f'{BIG_BASE}{ref["href"]}'
        migrate_thesis(url, output_dir, ongoing=False)


def migrate_phd_theses():
    url = f'{BIG_BASE}/teaching/phd-theses/'
    output_dir = CONTENT_DIR + '/phd-theses'

    r = s.get(url)
    raw_html = r.content.decode()
    soup = BeautifulSoup(raw_html, 'html.parser')
    ongoing_refs = soup.select('#main td[headers="thesisTitle ongoing"] a')
    finished_refs = soup.select('#main td[headers="thesisTitle finished"] a')

    for ref in ongoing_refs:
        url = ref["href"] if ref["href"].startswith('http') else f'{BIG_BASE}{ref["href"]}'
        migrate_thesis(url, output_dir, ongoing=True)

    for ref in finished_refs:
        url = ref["href"] if ref["href"].startswith('http') else f'{BIG_BASE}{ref["href"]}'
        migrate_thesis(url, output_dir, ongoing=False)


def migrate_projects():
    url = f'{BIG_BASE}/projects/'
    output_dir = CONTENT_DIR + '/phd-theses'


def main():
    # migrate_people()
    # migrate_visitors_and_friends()
    # migrate_master_theses()
    # migrate_phd_theses()
    migrate_projects()


if __name__ == '__main__':
    main()
