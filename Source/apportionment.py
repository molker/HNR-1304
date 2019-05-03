import math

def stanQuot0(sp, tp, seatnum):
	return float((sp / tp) * seatnum)

def stanQuot1(sp, tp, seatnum):
	return float(sp/(tp/seatnum))

def maxFrac():
	global sq
	stringSQ = []
	decimals = []
	for x in sq:
		stringSQ.append(str(x))
	for y in stringSQ:
		split = y.split(".")
		decimals.append(int(split[1][0:4]))
	m = max(decimals)
	for z in range(len(decimals)):
		if m == decimals[z]:
			mi = z
			break
	return mi

def hamMethod(seatnum):
	global population
	global seats
	global sq

	total = sum(population)

	for x in range(len(population)):
		sq.append(stanQuot0(population[x],total,seatnum))

	for x in range(len(sq)):
		seats.append(math.floor(sq[x]))

	cnt = 0
	while(sum(seats) != seatnum):
		rnd = maxFrac()
		seats[rnd] = seats[rnd] + 1
		sq[rnd] = seats[rnd]
		cnt += 1
	print seats
	print str(sum(seats)) + " seats"

def hillsMethod(sd):
	global population
	global seats
	global sq
	geo = []

	for x in population:
		sq.append(x/sd)

	for x in sq:
		geo.append(math.sqrt(math.ceil(x)*math.floor(x)))

	for x in range(len(sq)):
		seats.append(0)
		if sq[x] < geo[x]:
			seats[x] = math.floor(sq[x])
		else:
			seats[x] = math.ceil(sq[x])

	print seats
	print str(sum(seats)) + " seats"


 
population = []
seats = []
sq = []
total = float(0)

while True:
	try:
		line = raw_input()
		population.append(float(line))
	#stop when end of file is found
	except EOFError:
		break 

total = sum(population)

hillsMethod(139)
# SD 37084
# jeff = []
# div = 34500
# for x in population:
# 	jeff.append(math.floor(x/div))
# print "Jefferson's Method"
# print jeff
# print sum(jeff)

# print "Hamilton's Method"
# hamMethod(105)
