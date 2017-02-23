import random
import bisect

#@timeProfiling.timefn

@profile
def mainR():
	important_numbers = []
	for x in range(100000):
		new_number = random.randint(0, 1000)
		important_numbers.append(new_number)
	important_numbers.sort()


@profile
def mainRB():
	important_numbers = []
	for x in range(100000):
		new_number = random.randint(0, 1000)
		bisect.insort(important_numbers, new_number)
	print(find_closest(important_numbers, 300))

@profile	
def find_closest(haystack, needle):
	i = bisect.bisect_left(haystack, needle)
	if i == len(haystack):
		return i - 1
	elif haystack[i] == needle:
		return i
	elif i > 0: 
		j = i - 1
		# since we know the value is larger than needle (and vice versa for the
		# value at j), we don't need to use absolute values here
		if haystack[i] - needle > needle - haystack[j]:
			return j
		return i

@profile
def checkInsert(numList, x):
	L = numList(x)
	G = [1, 2, 3, 4, 5, 6]
	for x in range(x):
		randNum = random.randint(0, 1000)
		if randNum in L and randNum not in G:
			L.index(randNum)
		else:
			pass
@profile
def createList(x):
	numList = []
	for x in range(x):
		new_number = random.randint(0, 1000)
		numList.append(new_number)
	return numList

checkInsert(createList, 10000)






