__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.
def compare(x, y):
	if x > y:
		return 1
	if x == y:
		return 1
	if x < y:
		return -1
x = input("Input X: ")
y = input("Input Y: ")
result = compare(x, y)
print result