from pyairtable import Table
from string import Template
import shutil
import os

dir_path = "../_gyms"

table = Table(os.environ['AIRTABLE_API_KEY'], 'appKA1pVlbBOmxG4Z', 'Gyms')

t = Template("""---
_id: $id
title: $title
layout: gym
region: $region
city: $city
address: $address
latitude: $latitude
facebook: $facebook
instagram: $instagram
longitude: $longitude
email: $email
phone: $phone
website: $website
annual_fee: $annual_fee
ingress_price: $ingress_price
monthly_subscription_price: $monthly_subscription_price
structures: $structures
staff: $staff
rent: $rent
image: $image
---
$content
""")


os.mkdir(dir_path)


gyms = list(map(lambda g: g['fields'], table.all()))
for item in table.all():
    gym  = item['fields']
    filename = dir_path + "/" + gym.get('id') + ".md"
    image_url = gym['image'][0]['url'] if gym.get('image', False) else ""
    markdown = t.substitute({
        'id' : item['id'],
        'title' : gym.get('name', ''),
        'region': gym.get('region', ''),
        'city': gym.get('city', ''),
        'email': gym.get('email', ''),
        'address': gym.get('address', ''),
        'website': gym.get('website', ''),
        'phone': gym.get('phone', ''),
        'facebook': gym.get('facebook', ''),
        'instagram': gym.get('instagram', ''),
        'latitude': gym.get('latitude', ''),
        'longitude': gym.get('longitude', ''),
        'content': gym.get('content', ''),
        'annual_fee': gym.get('annual_fee', ''),
        'ingress_price': gym.get('ingress_price', ''),
        'monthly_subscription_price': gym.get('monthly_subscription_price', ''),
        'structures': ','.join(gym.get('structures', [])),
        'rent': ','.join(gym.get('rent', [])),
        'staff': ','.join(gym.get('staff', [])),
        'image': image_url
    })
    f = open(filename, "w")
    f.write(markdown)
    f.close()

# shutil.rmtree(dir_path)
# os.rename(dir_path + "_tmp", dir_path)
