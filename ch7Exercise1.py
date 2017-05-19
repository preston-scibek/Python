__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Rewrite the function print_n from Section 5.8 using iteration instead of recursion.
#def countdown(n):
#    if n <= 0:
#        print 'Blastoff!'
#    else:
#        print n
#
#def print_n(s, n):
#    if n <= 0:
#        return
#    print s
#    print_n(s, n-1)
def better_print_n(s, n):
	while n >= 0:
		print s
		n= n - 1
	return
word = raw_input("Enter string to be printed: ")
x = input("Enter number of times to print: ")
better_print_n(word, x)