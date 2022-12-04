with open('Day1/input.txt') as f:
    lines = f.readlines()

m = 0
s = 0
for calories in lines:
    if(calories == '\n'):
        if(m<s): m=s
        s = 0
    else:
        s += int(calories)
print(m)
