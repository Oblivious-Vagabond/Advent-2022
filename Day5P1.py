with open('Day5/test.txt') as f:
    lines = f.readlines()

# f = 0
# stacks = int(len(lines[0])/4)
# stack = [[] for i in range(stacks)]
# for i,l in enumerate(lines):
#     if (f==0):
#         if(lines[i+1]=='\n'):
#             f=1
#             continue
#         for sta,b in enumerate([l[s*4+1] for s in range(stacks)]):
#             if b != ' ': stack[sta].insert(0,b)
#     else:
#         if(l=='\n'): continue
#         [num,s,e] = [int(n) for n in l.strip('\n').split()[1::2]]
#         for n in range(num):
#             stack[e-1].append(stack[s-1].pop())
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
