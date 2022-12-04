lines = open("input.txt","r").readlines()

def calcPriority(char):
	priority = 0
	if char.isupper() : 
		char = char.lower()
		priority += 26
	priority += ord(char)-96
	return priority

total = 0

for i in range(0,len(lines),3):
	line1 = set(lines[i].strip())
	line2 = set(lines[i+1].strip())
	line3 = set(lines[i+2].strip())
	intersection = line1.intersection(line2.intersection(line3))
	total += calcPriority(intersection.pop())
print(total)
