import urllib.request, urllib.error, urllib.parse
import json

address = input("Enter a location: ")

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

api_key = 42

parms = dict() # the dictionary is used to be a part the the URL later
parms['address'] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms) #form the URL

print('Retrieving URL: ', url)
file = urllib.request.urlopen(url) #retrieve the URL data
data = file.read().decode() #read and decode the data because the data is in UTF-8 form

print('Retrieved', len(data), 'characters')

jsondata = json.loads(data)#load the data into python data using json.loads
address_id = jsondata['results'][0]['place_id'] #find the place of place_id just like in dictionary
print(address_id)
