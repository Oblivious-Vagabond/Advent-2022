with open('Day2/input.txt') as f:
    lines = f.readlines()

s = 0
for l in lines:
    [a,z] = [ord(x)-65 for x in l.strip("\n").split(" ")]
    s += (z-23)%3*3
    s += (a+(z-23)%3-1)%3+1
print(s)