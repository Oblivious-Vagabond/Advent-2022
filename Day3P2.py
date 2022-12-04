with open('Day3/input.txt') as f:
    lines = f.readlines()

s = 0
for g in range(0,len(lines),3):
    [e1,e2,e3] = [(ord(x)-96 for x in [*l.strip("\n")]) for l in lines[g:g+3]]
    p = next(iter(set(e1)&set(e2)&set(e3)))
    p = p if p>0 else p+58
    s += p
print(s)