import re
file = open('regex_sum_687324.txt')
s = 0
for line in file:
    y = [int(i) for i in re.findall('[0-9]+', line)]
    s = s + sum(y)
print(s)

#list comprehension version
file = open('regex_sum_687324.txt')
print(sum( [ int(i) for i in re.findall('[0-9]+', open('regex_sum_687324.txt').read())]))
