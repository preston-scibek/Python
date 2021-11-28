__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a
# right triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go.
from math import *

#def hypotenuse(a, b):
#	return 0.0

#def hypotenuse(a, b):
#	x = a**2
#	y = b**2
#	print "x = %d" %x
#	print "Y = %d" %y
#	return 0.0

#def hypotenuse(a, b):
#	x = a**2
#	y = b**2
#	print "x = %d" %x
#	print "Y = %d" %y
#	csquared = x + y
#	print "Y^2 = %d" %csquared
#	return 0.0

#def hypotenuse(a, b):
#	x = a**2
#	y = b**2
#	print "x = %d" %x
#	print "Y = %d" %y
#	csquared = x + y
#	print "Y^2 = %d" %csquared
#	c = sqrt(csquared)
#	print "C = %d" %c
#	return 0.0

#def hypotenuse(a, b):
#	x = a**2
#	y = b**2
#	print "x = %d" %x
#	print "Y = %d" %y
#	csquared = x + y
#	print "Y^2 = %d" %csquared
#	c = sqrt(csquared)
#	print "C = %d" %c
#	return c
	
def hypotenuse(a, b):
	x = a**2
	y = b**2
	csquared = x + y
	c = sqrt(csquared)
	return c
x = input("Input side A: ")
y = input("Input side B: ")
print "The hypotenuse of a triangle with sides: %d, %d = %d" %(x, y, hypotenuse(x, y))
