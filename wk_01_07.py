max = None
min = None
while True:
    number = input("input a integer: ")
    if number == 'done':
        break
    try:
        number = int(number)
    except:
        print("Invalid input")
        continue
    if max is None:
        max = number
    elif number > max:
        max = number
    if min is None:
        min = number
    elif number < min:
        min = number

print("Maximum is ", max)
print("Minimim is ", min)
