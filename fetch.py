import requests
import json

DATA_DIR = 'data'

PEOPLE_FILE = 'people.json'

PEOPLE_URL = 'https://tiss.tuwien.ac.at/api/orgunit/v22/id/4760?persons=true'

s = requests.Session()

r = s.get(PEOPLE_URL)
data = r.json()
people = data['employees']

with open(DATA_DIR + '/' + PEOPLE_FILE, 'w') as people_file:
    json.dump(people, people_file, indent=4)
