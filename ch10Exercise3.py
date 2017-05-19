__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Exercise 3  
#Write a function that takes a list of numbers and returns
# the cumulative sum; that is, a new list where the ith element 
#is the sum of the first i+1 elements from the original list.
# For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
def function_adder(num_list):
	counter = 0
	result = []
	for indice, i in enumerate(num_list):
		counter+=i
		result.append(counter)
	return result
number_list = [1,2,3,4,5,6,7,8,9]
print function_adder(number_list)