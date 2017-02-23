import dis

def fn_terse(upper = 1000000):
	return sum(range(upper))
	print("Functions return the same result:", fn_expressive() == fn_terse())

dis.dis(fn_terse)
