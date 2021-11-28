__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
from Exercise2 import better_square_root, bttr_square_root
from math import sqrt
#To test the square root algorithm in this chapter, you could compare it with math.sqrt. Write a function named test_square_root that prints a table like this:
#1.0 1.0           1.0           0.0
#2.0 1.41421356237 1.41421356237 2.22044604925e-16
#3.0 1.73205080757 1.73205080757 0.0
#4.0 2.0           2.0           0.0
#5.0 2.2360679775  2.2360679775  0.0
#6.0 2.44948974278 2.44948974278 0.0
#7.0 2.64575131106 2.64575131106 0.0
#8.0 2.82842712475 2.82842712475 4.4408920985e-16
#9.0 3.0           3.0           0.0
#
#The first column is a number, a; the second column is the square root of a 
#computed with the function from Section 7.5; the third column is the square root
# computed by math.sqrt; the fourth column is the absolute value of the
# difference between the two estimates.
def test_square_root():
	for num in range(10):
		real_num = num + 1.0
		print real_num, better_square_root(real_num, 10), sqrt(real_num), abs(better_square_root(real_num, 10) - sqrt(real_num))
test_square_root()