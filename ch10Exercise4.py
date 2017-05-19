__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Exercise 4  
#Write a function called middle that takes a list and returns a new list that 
#contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
def middle(listy):
	res = []
	for i, elem in enumerate(listy):
		if i == 0:
			continue
		if i == len(listy)-1:
			continue
		else:
			res.append(elem)
	return res
num_list = [1,2,3,"hi", "bye", "why", [1,2,3], ['a', 'b', 'c'], '3', '2', '1', 4, 5, 6]
print middle(num_list)