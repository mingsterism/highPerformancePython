import random
@profile
def checkInsert(numList):
	L = numList()
	for x in range(100):
		randNum = random.randint(0, 1000)
		if randNum in L:
			print(L.index(randNum))
@profile
def createList():
	numList = []
	for x in range(100):
		new_number = random.randint(0, 1000)
		numList.append(new_number)
	return numList

checkInsert(createList)

