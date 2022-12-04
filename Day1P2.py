with open('Day1/input.txt') as f:
    lines = f.readlines()

s = 0
elves = []
for calories in lines:
    if(calories == '\n'):
        elves.append(s)
        s = 0
    else:
        s += int(calories)
elves.sort(reverse=True)
print(sum(elves[0:3]))