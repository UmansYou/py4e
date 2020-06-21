import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET

url = input("Enter - ")
fhandle = urllib.request.urlopen(url).read()

file = ET.fromstring(fhandle)

lst = file.findall('comments/comment') #create a list of trees of comment 

numbers = list() #create a list for the numbers
for item in lst:
    number = item.find('count').text #extract the text of 'count' from each of the tag
    number = int(number)
    numbers.append(number)

print(sum(numbers))
