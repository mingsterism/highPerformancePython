import dis


def fn_expressive(upper = 1000000):
	total = 0
	for n in range(upper):
		total += n
	return total

dis.dis(fn_expressive)