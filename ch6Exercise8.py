__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#The greatest common divisor (GCD) of a and b is the largest num + 1ber 
#that divides both of them with no remainder.
#One way to find the GCD of two num + 1bers is based on the observation that 
#if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r).
# As a base case, we can use gcd(a, 0) = a.

#Write a function called gcd that takes parameters a and b
# and returns their greatest common divisor.

def gcd(a, b):
	greatest_num = 0
	if a > b:
		for num in range(a):
			if a %( num + 1) == 0 and b % (num + 1) == 0:
				greatest_num = num+1
	if b >= a:
		for num in range(b):
			if a % (num + 1) == 0 and b % (num + 1) == 0:
				greatest_num = num+1
	return greatest_num
a = input("Enter a: ")
b = input("Enter b: ")
print gcd(a, b)