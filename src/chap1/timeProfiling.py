from functools import wraps 
import timeit

def timefn(fn):
	@wraps(fn)
	def measure_time(*args, **kwargs):
		t1 = timeit.timeit()
		result = fn(*args, **kwargs)
		t2 = timeit.timeit()
		print ("@timefn:" + fn.__name__ + " took " + str(t2 - t1) + " seconds")
		return result
	return measure_time