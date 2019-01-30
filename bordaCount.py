'''
1/18/2019
Activity 2 Borda Count Method Problem
'''
# Create all the different arrays
candidates = []
scores = []
numVotes = []
weights = []
rows = []

# Get input describing the preference schedule 
numCan = input()
numRow = input()
numCol = input()

# Loops that will fill the arrays
i = 65

for x in range(numCan):
	candidates.append(chr(i))
	scores.append(0)
	i = i + 1

for x in range(numCol):
	numVotes.append(input())

for x in range(numRow):
	weights.append(numRow - x)

for x in range(numRow):
	row = raw_input()
	rows.append(row)

# Calculate the scores for the candidates based on the rows
for x in range(numRow):
	for y in range(numCol):
		if rows[x][y] == "A":
			scores[0] += numVotes[y] * weights[x]
		if rows[x][y] == "B":
			scores[1] += numVotes[y] * weights[x]
		if rows[x][y] == "C":
			scores[2] += numVotes[y] * weights[x]
		if rows[x][y] == "D":
			scores[3] += numVotes[y] * weights[x]

# Print out the scores
for x in range(numCan):
	print candidates[x] + ": " + str(scores[x])  

