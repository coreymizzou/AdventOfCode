f = open('day1input.txt')
floor = f.readline()
    
y = 0

for x in floor:
    if x == '(':
        y += 1
    elif x == ')':
        y -= 1
print(y)
