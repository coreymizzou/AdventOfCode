with open('text.txt') as f:
  paper = f.readlines()

totalPaper = 0
ribbon = 0
  
for line in paper:
  l, w, h = map(int, line.split('x'))
  totalPaper += (2*l*w + 2*w*h + 2*h*l) + min(l*w, w*h, h*l)
  ribbon += min(l,w,h)*2 + sorted([l,w,h])[1] * 2 + (l*w*h)
  
print(totalPaper)
print(ribbon)
