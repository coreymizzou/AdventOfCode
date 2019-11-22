f = open('day1input.txt')
floor = f.readline()

#part 1
y = 0
for x in floor:
    if x == '(':
        y += 1
    elif x == ')':
        y -= 1
print(y)

#part 2
y = 0
count = 0
for x in floor:
    if y >= 0:
        if x == '(':
            y += 1
        elif x == ')':
            y -= 1
        count += 1
print(count)
