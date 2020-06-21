import urllib.request, urllib.error, urllib.parse
import json

url = input("Enter - ")
fhandle = urllib.request.urlopen(url).read()

data = json.loads(fhandle) #load the json data into python data

lst = list()
comments = data["comments"] #retrieve the 'comments' in the json data
for item in comments:
    count = item['count']
    count = int(count)
    lst.append(count)

print(sum(lst))
