lines = open("input.txt","r").readlines()

currTotal = 0
topelf = 0

for line in lines:
	line = line.strip()
	if line == "":
		if currTotal > topelf:
			topelf = currTotal
		currTotal = 0
	else:
		currTotal += int(line)
print(topelf)