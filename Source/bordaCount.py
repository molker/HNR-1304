'''
1/18/2019
Activity 2 Borda Count Method Problem
	Has now been upgaded to work for any size table
'''
# Create all the different arrays
candidates = []
numVotes = []
rows = []
scores = []
weights = []

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
	weights.append(numRow - x -1)

for x in range(len(rows)):
	for y in range(len(rows[x])):
		diff = True
		for c in candidates:
			if rows[x][y] == c: 
				diff = False
		if diff == True and rows[x][y] != "#":
			candidates.append(rows[x][y])
			scores.append(0)

# Calculate the scores for the candidates based on the rows
for x in range(numRow):
	for y in range(len(rows[x])):
		for z in range(len(candidates)):
			if rows[x][y] == candidates[z]:
				scores[z] += numVotes[y] * weights[x]
			elif rows[x][y] == "#":
				scores[z] += 0

win = max(scores)
# Print out the scores
for x in range(len(candidates)):
	if scores[x] == win:
		winc = candidates[x]
	print candidates[x] + ": " + str(scores[x]) 
print winc + " Wins with " + str(win) + " points"

