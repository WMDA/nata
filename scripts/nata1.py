import requests
import re

url='http://natas1.natas.labs.overthewire.org'
username='natas1'
password='gtVrDuiDfck831PqWsLEZy5gyDz1clto'

website=requests.get(url,auth=(username,password))
print(re.findall('<!--The password for natas2 is (.*) -->',website.text))