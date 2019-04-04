'''
3/8/2019
Instant Runoff Voting Method
'''

'''
function: checkMajority
parameters:
	rows - every row of the preference table votes
	numVotes - the corresponding votes to the position in the table
	candidates - a list of candidates 
result:
	will return either the candidate with the majority vote or a -1 to 
	signify nobody has a majority yet
'''
def checkMajority(rows, numVotes, candidates):
	fpVotes = []
	total = 0
	global majority
	for x in range(len(candidates)):
		fpVotes.append(0)
	for x in range(len(numVotes)):
		if rows[0][x] == "#":
			found = False
			for y in range(len(rows)):
				if rows[y][x] != "#" and found != True:
					fpVotes[ord(rows[y][x]) - 65] += int(numVotes[x])
					found = True
		else:
			fpVotes[ord(rows[0][x]) - 65] += int(numVotes[x])
	for x in fpVotes:
		total += x
	for x in range(len(fpVotes)):
		check = float(fpVotes[x]) / float(total)
		if check > 0.5:
			majority = True
			return x
	return -1

'''
function: checkFP 
parameters:
	rows - every row of the preference table votes
	numVotes - the corresponding votes to the position in the table
	candidates - a list of candidates 
result:
	will return the candidate who currently has the least first place votes
	so the program can remove them to continue the instant runoff
'''
def checkFP(rows, numVotes, candidates):
	fpVotes = []
	count = 0
	global top3
	for x in range(len(candidates)):
		fpVotes.append(0)
	for x in range(len(numVotes)):
		if rows[0][x] == "#":
			found = False
			for y in range(len(rows)):
				if rows[y][x] != "#" and found != True:
					fpVotes[ord(rows[y][x]) - 65] += int(numVotes[x])
					found = True
		else:
			fpVotes[ord(rows[0][x]) - 65] += int(numVotes[x])
	for x in range(len(fpVotes)):
		if fpVotes[x] == 0:
			fpVotes[x] = "#"
	lose = min(fpVotes)
	for x in fpVotes:
		if x != "#":
			count += 1
	if count < 4:
		top3 = True
	for x in range(len(candidates)):
		if fpVotes[x] == lose:
			result = candidates[x]
	return result

'''
function: dump
parameters:
	rows - every row of the preference table votes
	numVotes - the corresponding votes to the position in the table
result:
	prints out the preference schedule in the same format as how it was input
'''
def dump(rows, numVotes):
	for x in range(len(numVotes)):
		blank = 0
		result = ""
		result += numVotes[x] + " "
		for y in range(len(rows)):
			if rows[y][x] == "#":
				blank += 1
			else: 
				result += rows[y][x] + " "	
		if blank != 3:
			print result + "\n"

# Create all the different arrays
candidates = []
numVotes = []
rows = []

# reading in the input
while True:
	try:
		line = raw_input()
		line = line.split(" ")
		vote = line[0]
		row = line[1]
		#add blanks for ballots with less than 3 candidates listed
		if len(row) < 3:
			for x in range(3 - len(row)):
				row += "#"
		numVotes.append(vote)
		#make sure the rows have room for each ballot before adding them
		if len(rows) < len(row):
			for x in range(len(row)-len(rows)):
				rows.append("");
		for x in range(len(row)):
			rows[x] += row[x]
	#stop when end of file is found
	except EOFError:
		break
#makes the candidate list 
for x in range(len(rows)):
	for y in range(len(rows[x])):
		diff = True
		for c in candidates:
			if rows[x][y] == c: 
				diff = False
		if diff == True and rows[x][y] != "#":
			candidates.append(rows[x][y])
#"globals" used in the functions as flags
top3 = False
majority = False
#while loop for doing the IRV method
while checkMajority(rows, numVotes, candidates) == -1 and top3 == False:
	losec = checkFP(rows, numVotes, candidates)
	for x in range(len(rows)):
		for y in range(len(rows[x])):
			if rows[x][y] == losec:
				tmp = list(rows[x])
				tmp[y] = "#"
				rows[x] = "".join(tmp)
#Checks when flag is set for the result to print
if majority == True:
	print "Win by Majority:"
	win = candidates[checkMajority(rows, numVotes, candidates)]
	print win + " Wins"
elif top3 == True: 
	print "Top 3 Preference Table"
	dump(rows, numVotes)
