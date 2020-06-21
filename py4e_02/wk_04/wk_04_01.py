fname = input("Enter file name: ")
file = open(fname)
lst = list()
for line in file:
    line = line.split()
    for word in line:
        if not word in lst:
            lst.append(word)
lst.sort()
print (lst)
