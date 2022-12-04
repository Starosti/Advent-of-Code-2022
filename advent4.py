import re
lines = open("input4.txt","r").readlines()

pairs = 0
for line in lines:

	match =re.search("(\d{0,3})-(\d{0,3}),(\d{0,3})-(\d{0,3})",line)
	firstRange = [int(match.group(1)),int(match.group(2))]
	secondRange = [int(match.group(3)),int(match.group(4))]

	if (firstRange[0] >= secondRange[0] and firstRange[1] <= secondRange[1]) or (firstRange[0] <= secondRange[0] and firstRange[1] >= secondRange[1]):
		pairs += 1

print(pairs)