with open('Day5/test.txt') as f:
    lines = f.readlines()

start = 0
stacks = int(len(lines[0])/4)
stack = [[] for i in range(stacks)]
for i in range(len(lines)):
    if(lines[i+1]=='\n'):
        start = i+2
        break
    for sta,b in enumerate([lines[i][s*4+1] for s in range(stacks)]):
        if b != ' ': stack[sta].insert(0,b)

for l in lines[start:]:
    [num,s,e] = [int(n) for n in l.strip('\n').split()[1::2]]
    for n in range(num):
        stack[e-1].append(stack[s-1].pop())

out = ''
for s in stack:
    out += s.pop()
print(out)
