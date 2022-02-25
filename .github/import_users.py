from pyairtable import Table
from string import Template
import shutil
import os

dir_path = "../_users"

table = Table(os.environ['AIRTABLE_API_KEY'], 'appKA1pVlbBOmxG4Z', 'Users')

t = Template("""---
title: $title
_id: $id
username: $username
layout: user
email: $email
phone: $phone
titles: $titles
gyms: $gyms
---
$content
""")


os.mkdir(dir_path)

for item in table.all():
    gym = item['fields']
    filename = dir_path + gym.get('username') + ".md"
    markdown = t.substitute({
        'title' : gym.get('name', ''),
        'username' : gym.get('username', ''),
        'email': gym.get('email', ''),
        'phone': gym.get('phone', ''),
        'content': gym.get('content', ''),
        'titles': ','.join(gym.get('titles', [])),
        'gyms': ','.join(gym.get('gyms', [])),
        'id': item['id']
    })
    f = open(filename, "w")
    f.write(markdown)
    f.close()

# shutil.rmtree(dir_path)
# os.rename(dir_path + "_tmp", dir_path)
