fname = input("Enter file name: ")
file = open(fname)
emails = list()
for line in file:
    if line.startswith('From '):
        txt = line.split()
        emails.append(txt[1])
for email in emails:
    print(email)
print("There were", len(emails), "lines in the file with From as the first word")
