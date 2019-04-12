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
		print split[1][0:4]
		decimals.append(split[1][0:4])
	m = max(decimals)
	for z in range(len(decimals)):
		if m == decimals[z]:
			mi = z
	return z

def hamMethod(seatnum):
	global population
	global seats
	global sq

	total = sum(population)

	for x in range(len(population)):
		sq.append(stanQuot0(population[x],total,seatnum))

	for x in range(len(sq)):
		seats.append(math.floor(sq[x]))

	while(sum(seats) != seatnum):
		rnd = maxFrac()
		seats[x] = seats[x] + 1
		sq[x] = seats[x]
	print seats
	print sum(seats)



# def jeffMethod(seatnum):



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
# for x in population:
# 	tmp = float(x/total)
# 	print '{:.6}'.format(x/(1000))
# 	seats.append(math.ceil(x/(1100)))
# print seats
# print sum(seats)