with open('Day3/input.txt') as f:
    lines = f.readlines()

s = 0
for l in lines:
    b = [ord(x)-96 for x in [*l.strip("\n")]]
    m = int(len(b)/2)
    p = next(iter(set(b[:m])&set(b[m:])))
    p = p if p>0 else p+58
    s += p
print(s)