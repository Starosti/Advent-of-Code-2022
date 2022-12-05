import re
lines = open("input5.txt","r").readlines()

stacks = []

for i in range(9):
	stacks.append([])

for i in range(7,-1,-1):
	match = re.findall("(?:   |(?:\[?([A-Z])\])?) ?",lines[i])
	for j in range(9):
		if match[j]:
			stacks[j].append(match[j])

for i in range(10,len(lines)):
	line = lines[i].strip()
	match = re.findall("move (\d{1,2}) from (\d) to (\d)",line)[0]
	moveFrom = int(match[1])-1;
	moveTo = int(match[2])-1;
	moveCount = int(match[0]);
	elems = stacks[moveFrom][-moveCount:]
	stacks[moveFrom] = stacks[moveFrom][:-moveCount]
	stacks[moveTo].extend(elems)

for i in range(9):
	print(stacks[i].pop(),end="")