'''
1/18/2019
Activity 2 Borda Count Method Problem
	Has now been upgaded to work for any size table
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
i = 65	# the ASCII value for A

for x in range(numCan):
	candidates.append(chr(i))
	scores.append(0)
	i = i + 1

for x in range(numCol):
	numVotes.append(input())

for x in range(numRow):
	row = raw_input()
	rows.append(row)
	weights.append(numRow - x)

# Calculate the scores for the candidates based on the rows
for x in range(numRow):
	for y in range(numCol):
		for z in range(numCan):
			if rows[x][y] == candidates[z]:
				scores[z] += numVotes[y] * weights[x]
			elif rows[x][y] == "#":
				scores[z] += 0

# Print out the scores
for x in range(numCan):
	print candidates[x] + ": " + str(scores[x])  

