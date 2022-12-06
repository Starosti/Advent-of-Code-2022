line = open("input6.txt","r").readlines()[0]
chars = list(line)

def checkDuplicate(chrList):
	return len(set(chrList)) != len(chrList)

for i in range(len(chars)):
	if not checkDuplicate({chars[i],chars[i+1],chars[i+2],chars[i+3]}):
		print(i+4)
		break
