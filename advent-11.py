#raw = ['5483143223','2745854711','5264556173','6141336146','6357385478','4167524645','2176841721','6882881134','4846848554','5283751526']
#raw = ['11111','19991','19191','19991','11111']
raw = ['7313511551','3724855867','2374331571','4438213437','6511566287','6727245532','3736868662','2348138263','2417483121','8812617112']

data = []

for row in raw:
	temp = []
	for n in row:
		temp.append(int(n))
	data.append(temp)

def step(data):
	for x in range(len(data)):
		for y in range(len(data[x])):
			data[x][y] += 1
	return evaluate(data, [], 0)

def evaluate(data, flashed, count):
	coords = []
	curr = []
	#identify those that are flashing
	for x in range(len(data)):
		for y in range(len(data[x])):
			if(data[x][y] > 9):
				data[x][y] = 0
				count += 1
				curr.append([x,y])
				flashed.append([x,y])

	for f in curr:
		coords.extend(coordHelper(data, f[0], f[1], flashed))

	if(len(coords) > 0):
		#print(coords)
		for c in coords:
			#print(c)
			data[c[0]][c[1]] += 1

		return evaluate(data, flashed, count)
	else:
		return [data,len(flashed),count]

def coordHelper(data, x, y, discount):
	coords = []
	top = x <= 0
	bottom = x+1 >= len(data)
	left = y <= 0
	right = y+1 >= len(data[x])

	if(not top and data[x-1][y] != 0):
		coords.append([x-1,y])

	if(not bottom and data[x+1][y] != 0):
		coords.append([x+1,y])

	if(not left and data[x][y-1] != 0):
		coords.append([x,y-1])
	if(not right and data[x][y+1] != 0):
		coords.append([x,y+1])

	if(not left and not top and data[x-1][y-1] != 0):
		coords.append([x-1,y-1])

	if(not right and not top and data[x-1][y+1] != 0):
		coords.append([x-1,y+1])

	if(not left and not bottom and data[x+1][y-1] != 0):
		coords.append([x+1,y-1])

	if(not right and not bottom and data[x+1][y+1] != 0):
		coords.append([x+1,y+1])

	#filter out any discounts
	output = []
	for v in coords:
		if v not in discount:
			output.append(v)

	return output

def checkAll(data):
	for row in data:
		for cell in row:
			if(cell != 0):
				return False

	return True


count = 0
n = 0
while(not checkAll(data)):
	out = step(data)
	data = out[0]
	count += out[2]
	n += 1
	print(n)

for row in data:
	print(row)

print(count)
print(n)