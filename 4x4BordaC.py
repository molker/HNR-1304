'''
1/18/2019
Activity 2 Borda Count Method Problem
'''

numVote0 = input("Votes 0:")
numVote1 = input("Votes 1:")
numVote2 = input("Votes 2:")
numVote3 = input("Votes 3:")
numVotes = [numVote0, numVote1, numVote2, numVote3]

'''
def switch_can(x):
	if x == "A"
candidates = ["A","B","C","D"]
scores = [0,0,0,0]

row0 = input("Row0:")
row1 = input("Row1:")
row2 = input("Row2:")
row3 = input("Row3:")

for x in range(4):

'''

FIRST = 3
SECOND = 2
THIRD = 1
FOURTH = 0

A = numVote0 * FIRST + numVote1 * FOURTH + numVote2 * FOURTH + numVote3 * FOURTH

B = numVote0 * THIRD + numVote1 * FIRST + numVote2 * SECOND + numVote3 * THIRD

C = numVote0 * FOURTH + numVote1 * THIRD + numVote2 * FIRST + numVote3 * SECOND

D = numVote0 * SECOND + numVote1 * SECOND + numVote2 * THIRD + numVote3 * FIRST

print "A: " + str(A)
print "B: " + str(B)
print "C: " + str(C)
print "D: " + str(D)

