lines = open("input3.txt","r").readlines()

def calcPriority(char):
	priority = 0
	if char.isupper() : 
		char = char.lower()
		priority += 26
	priority += ord(char)-96
	return priority

total = 0

for line in lines:
	line = line.strip()
	firstPart = set(line[:len(line)//2])
	secondPart = set(line[len(line)//2:])
	intersection = firstPart.intersection(secondPart)
	total += calcPriority(intersection.pop())
print(total)
