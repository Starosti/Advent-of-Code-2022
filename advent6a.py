line = open("input6.txt","r").readlines()[0]
chars = list(line)

def checkDuplicate(chrList):
	return len(set(chrList)) != len(chrList)

for i in range(len(chars)):
	signalMarkers = []
	for j in range(14):
		signalMarkers.append(chars[i+j])
	if not checkDuplicate(signalMarkers):
		print(i+14)
		break
