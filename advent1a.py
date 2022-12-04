lines = open("input1.txt","r").readlines()

topelf = []
currTotal = 0

for line in lines:
	line = line.strip()
	if line == "": 
		topelf.append(currTotal)
		currTotal = 0
	else:
		currTotal += int(line)
topelf.sort()
print(topelf[-1]+topelf[-2]+topelf[-3])