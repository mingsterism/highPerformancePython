import random
from src.chap1 import timeProfiling

@timeProfiling.timefn
def mainR(x):
	important_numbers = []
	for x in range(x):
		new_number = random.randint(0, 1000)
		important_numbers.append(new_number)



