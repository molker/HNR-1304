'''
2/6/2019
Pairwise Voting Method
'''
#function for pairwise comprison 
def pairwise(a, b, rows, numVotes):
	pairscore = [0, 0]
	for x in range(len(rows[0])):
		for y in range(len(rows)):
			if rows[y][x] == a:
				pairscore[0] += numVotes[x]
				break
			elif rows[y][x] == b:
				pairscore[1] += numVotes[x]
				break
	if pairscore[0] > pairscore[1]:
		return a
	else:
		return b


# Create all the different arrays
candidates = []
numVotes = []
rows = []
scores = []

# Get input describing the preference schedule 
numRow = input()

# Loops that will fill the arrays

numVotes = raw_input()
numVotes = numVotes.split(",")
for n in range(len(numVotes)):
	numVotes[n] = int(numVotes[n])

for x in range(numRow):
	row = raw_input()
	rows.append(row)

for x in range(len(rows)):
	for y in range(len(rows[x])):
		diff = True
		for c in candidates:
			if rows[x][y] == c: 
				diff = False
		if diff == True and rows[x][y] != "#":
			candidates.append(rows[x][y])
			scores.append(0)

# Put each candidate against each other
compared = []
for x in candidates:
	for y in candidates:
		if x != y:
			for z in compared:
				if sorted(str(x+y)) == z:
					break
			else:
				pwin = pairwise(x,y,rows,numVotes)
				compared.append(sorted(str(x+y)))
				scores[ord(pwin)-65] += 1

win = max(scores)
# Print out the scores
for x in range(len(candidates)):
	if scores[x] == win:
		winc = candidates[x]
print winc + " Wins with " + str(win) + " points"

