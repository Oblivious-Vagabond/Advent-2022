with open('Day4/input.txt') as f:
    lines = f.readlines()

os = 0
for l in lines:
    [a1,a2,b1,b2]=[int(x) for x in l.strip("\n").replace(',','-').split('-')]
    os += (a1<=b2) and (b1<=a2)
print(os)