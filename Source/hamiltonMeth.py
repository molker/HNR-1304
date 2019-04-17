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

tmptotal = 0
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

hamMethod(25)
