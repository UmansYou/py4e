fname = input("Enter file name:")
file = open (fname)

hours = dict()
for line in file:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        time = words[6]
        hour = time[:1]
        hours[hour] = hours.get(hour,0) +1

hours.sort()
for key, value in hours.items():
    print (key, value)
