import math
import random
import bisect

number = random.randint(0, 100)

def check_prime(number):
	sqrt_number = math.sqrt(number)
	number_float = float(number)
	for x in range(2, int(sqrt_number) + 1):
		if number_float % x == 0:
			return False
	return True

# for x in range(100):
# 	if check_prime(x) == True:
# 		print(x)
print(check_prime(10000000))
print(check_prime(10000019))