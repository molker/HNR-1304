'''
3/8/2019
Instant Runoff Voting Method
'''
#function for pairwise comprison 
def instant(a,b, rows, numVotes):
	pairscore = [0, 0]
	for x in range(len(rows[0])):
		for y in range(len(rows)):
			if rows[y][x] == a:
				pairscore[0] += int(numVotes[x])
				break
			elif rows[y][x] == b:
				pairscore[1] += int(numVotes[x])
				break
	if pairscore[0] > pairscore[1]:
		return a
	else:
		return b

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
	# print fpVotes
	lose = min(fpVotes)
	# print lose
	for x in fpVotes:
		if x != "#":
			count += 1
	if count < 4:
		top3 = True
	for x in range(len(candidates)):
		if fpVotes[x] == lose:
			result = candidates[x]
	return result

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
scores = []

while True:
	try:
		line = raw_input()
		line = line.split(" ")
		vote = line[0]
		row = line[1]
		if len(row) < 3:
			for x in range(3 - len(row)):
				row += "#"
		numVotes.append(vote)
		if len(rows) < len(row):
			for x in range(len(row)-len(rows)):
				rows.append("");
		for x in range(len(row)):
			rows[x] += row[x]
	except EOFError:
		break

for x in range(len(rows)):
	for y in range(len(rows[x])):
		diff = True
		for c in candidates:
			if rows[x][y] == c: 
				diff = False
		if diff == True and rows[x][y] != "#":
			candidates.append(rows[x][y])
			scores.append(0)
top3 = False
majority = False
while checkMajority(rows, numVotes, candidates) == -1 and top3 == False:
	losec = checkFP(rows, numVotes, candidates)
	for x in range(len(rows)):
		for y in range(len(rows[x])):
			if rows[x][y] == losec:
				tmp = list(rows[x])
				tmp[y] = "#"
				rows[x] = "".join(tmp)
if majority == True:
	print "Win by Majority:"
	win = candidates[checkMajority(rows, numVotes, candidates)]
	# print candidates
	print win + " Wins"
	# dump(rows, numVotes)
elif top3 == True: 
	print "Top 3 Preference Table"
	dump(rows, numVotes)
