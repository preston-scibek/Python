__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Fermat's Last Theorem says that there are no positive integers a, b, and c such that
#a^n + b^n = c^n 
#for any values of n greater than 2.
#Write a function named check_fermat that takes four parameters--a, b, c 
#and n--and that checks to see if Fermat's theorem holds. If n is greater than 2
# and it turns out to be true that
#a^n + b^n = c^n 
#the program should print, "Holy smokes, Fermat was wrong!" Otherwise the program should print, "No, that doesn't work."
#Write a function that prompts the user to input values for a, b, c and n, converts them to integers,
# and uses check_fermat to check whether they violate Fermat's theorem.
def check_fermat(a, b, c , n):
	if ((a**n) + (b**2)) == (c**n) and n>2:
		print "Holy smokes, Fermat was wrong!"
	else:
		print "No, that doesn't work."
def get_val_for_fermat():
	a = input("Enter value A: ")
	b = input("Enter value B: ")
	c = input("Enter value C: ")
	n = input("Enter value N: ")
	a = int(a)
	b = int(b)
	c = int(c)
	n = int(n)
	check_fermat(a,b,c,n)
get_val_for_fermat()