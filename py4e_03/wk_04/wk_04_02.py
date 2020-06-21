import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input("Enter - ")
#get the input for the number of time processing the loop
count = input("Enter count: ")
try:
    count = int(count)
except:
    print("invalid entry!")
#get the number of position and -1
pos = input("Enter position: ")
try:
    pos = int(pos)-1
except:
    print("invalid entry!")


loop = 1
#create a loop that run the number of time entered before, exit when reach the 'count'
while loop <= count :
    fhandle = urllib.request.urlopen(url).read()
    file = BeautifulSoup(fhandle, 'html.parser')

    tags = file('a')#retrieve the anchor tags
    tag = tags[pos]#retrieve the anchor tag in the position entered before
    url = tag.get('href', None).strip()#get the url that is in that anchor tag and put it into 'url' to use run again

    print ('retrieving: ', url)

    loop = loop + 1
