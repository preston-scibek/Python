__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Encapsulate this loop in a function called square_root that takes a as a parameter, 
#chooses a reasonable value of x, and returns an estimate of the square root of a.
def square_root(a):
	a = float(a)
	x = a + 1.0
	y = (x + (a/x)) / 2
	print "An estimate of the square root of %f = %f" %(a, y)
	return y
def bttr_square_root(a, b):
	a = float(a)
	x = b
	y = (x + (a/x)) / 2.0
	return y
def better_square_root(a, times):
	y = bttr_square_root(a, a+1)
	for num in range(times):
		y = bttr_square_root(a, y)
	return y
#print better_square_root(4, 10)	
	
if __name__ == "__main__":
	x = input("Enter number to be rooted: ")
	square_root(x)