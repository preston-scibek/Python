__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
#Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
# Note: you will have to think about the base case.

def is_power(a, b):	
	while(a%b == 0):
		a = a/b
	if a == 1.0:
		return True
	else:
		return False
a = input("Enter A: ")
b = input("Enter B: ")
print is_power(float(a), float(b))