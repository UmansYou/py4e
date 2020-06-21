import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Access the web data using urllib
url = input('Enter - ')
fhandle = urllib.request.urlopen(url).read()
file = BeautifulSoup(fhandle, 'html.parser') #Parse the file using BeautifulSoup

tags = file('span')
sum = 0
for tag in tags:
    tag = str(tag)
    number = re.findall("[0-9]+",tag)
    for x in number:
        x = int(x)
        sum = sum + x

print(sum)
