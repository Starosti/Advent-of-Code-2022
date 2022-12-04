lines = open("input2.txt","r").readlines()

def rpsWinner(p1,p2):
	if p1 == "A": # p1 -> rock
		if p2 == "A": # p2 -> rock -> Draw
			return 0
		if p2 == "B": # p2 -> paper -> Win
			return 1
		if p2 == "C": # p2 -> scissors -> Lose
			return -1
	if p1 == "B": # p1 -> paper
		if p2 == "A": # p2 -> rock -> Lose
			return -1
		if p2 == "B": # p2 -> paper -> Draw
			return 0
		if p2 == "C": # p2 -> scissors -> Win
			return 1
	if p1 == "C": # p1 -> scissors
		if p2 == "A": # p2 -> rock -> Win
			return 1
		if p2 == "B": # p2 -> paper -> Lose
			return -1
		if p2 == "C": # p2 -> scissors -> Draw
			return 0

def calculateMove(p1,cond):
	if cond == "X": # LOSE
		if p1 == "A":
			return "C"
		if p1 == "B":
			return "A"
		if p1 == "C":
			return "B"
	if cond == "Y": # DRAW
		return p1
	if cond == "Z": # WIN
		if p1 == "A":
			return "B"
		if p1 == "B":
			return "C"
		if p1 == "C":
			return "A"

pointsTotal = 0

for line in lines:
	points = 0
	enemyMove = line[0]
	yourMove = calculateMove(enemyMove,line[2])
	match yourMove:
		case "A":
			points += 1
		case "B":
			points += 2
		case "C":
			points += 3
		case _:
			print("error")
	winner = rpsWinner(enemyMove,yourMove)
	match winner:
		case -1:
			points += 0
		case 0:
			points += 3
		case 1:
			points += 6
		case _:
			print("error")
	pointsTotal += points
print(pointsTotal)