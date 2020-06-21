fname = input("Enter the file name: ")
fhandle = open(fname)

# creating a dictionary to count sender
sender = dict()
for line in fhandle:
    line = line.strip()
    # count the second word if the line starts with 'From'
    if line.startswith('From '):
        word = line.split()
        address = word[1]
        sender[address] = sender.get(address,0) + 1

#Loop through the dictionary to find the name and count
name = None
count = None
for key, value in sender.items():
    if name == None or count < value:
        name = key
        count = value

print(name, count)
