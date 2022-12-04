lines = open("input2.txt","r").readlines()

def rpsWinner(p1,p2):
	if p1 == "A": # p1 -> rock
		if p2 == "X": # p2 -> rock -> Draw
			return 0
		if p2 == "Y": # p2 -> paper -> Win
			return 1
		if p2 == "Z": # p2 -> scissors -> Lose
			return -1
	if p1 == "B": # p1 -> paper
		if p2 == "X": # p2 -> rock -> Lose
			return -1
		if p2 == "Y": # p2 -> paper -> Draw
			return 0
		if p2 == "Z": # p2 -> scissors -> Win
			return 1
	if p1 == "C": # p1 -> scissors
		if p2 == "X": # p2 -> rock -> Win
			return 1
		if p2 == "Y": # p2 -> paper -> Lose
			return -1
		if p2 == "Z": # p2 -> scissors -> Draw
			return 0

pointsTotal = 0

for line in lines:
	points = 0
	enemyMove = line[0]
	yourMove = line[2]
	match yourMove:
		case "X":
			points += 1
		case "Y":
			points += 2
		case "Z":
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