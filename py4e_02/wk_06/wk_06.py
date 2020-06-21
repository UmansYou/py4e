fname = input("Enter file name:")
file = open (fname)

hours = dict()
for line in file:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time[:2]
        hours[hour] = hours.get(hour,0) +1


for key, value in sorted(hours.items()):
    print (key, value)
