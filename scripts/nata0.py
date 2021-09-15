import requests
import re

url='http://natas0.natas.labs.overthewire.org'
username='natas0'
password='natas0'

website=requests.get(url,auth=(username,password))
print(re.findall('<!--The password for natas1 is (.*) -->',website.text))