import random
import bisect
from src.chap1 import timeProfiling

def find_closest(haystack, needle):
	#bisect.bisect_left will return the first value int he ahystack that is greater
	#than the needle
	i = bisect.bisect_left(haystack, needle)
	if i == len(haystack):
		return i - 1 
	elif haystack[i] == needle:
		return i 
	elif i > 0:
		j = i - 1 
		if haystack[i] - needle > needle - haystack[j]:
			return j 
	return i 


@timeProfiling.timefn
def mainR(x):
	important_numbers = []
	for i in range(x):
		new_number = random.randint(0, 1000)
		bisect.insort(important_numbers, new_number)
	# important_numbers will already be in order because we inserted new elements
	# with bisect.insort
	# print(important_numbers)
	closest_index = find_closest(important_numbers, -250)
	print("Closest value to -250: ", important_numbers[closest_index])
	closest_index = find_closest(important_numbers, 500)
	print("Closest value to 500: ", important_numbers[closest_index])
	closest_index = find_closest(important_numbers, 1100)
	print("Closest value to 1100: ", important_numbers[closest_index])

