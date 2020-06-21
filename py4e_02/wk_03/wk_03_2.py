# Use the file name mbox-short.txt as the file name
fname = input("Please enter the file name: ")
file = open(fname)
count = 0
sum = 0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        number = line[pos+1:].rstrip()
        count = count + 2
        sum = sum + float(number)
print ("Average spam confidence: ", sum/count)
