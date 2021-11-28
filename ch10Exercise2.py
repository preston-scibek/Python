__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Sometimes you want to traverse one list while building another.
# For example, the following function takes a list of strings and 
# returns a new list that contains capitalized strings:
#def capitalize_all(t):
#    res = []
#    for s in t:
#        res.append(s.capitalize())
#    return res
#res is initialized with an empty list; each time through the loop,
# we append the next element. So res is another kind of accumulator.
#An operation like capitalize_all is sometimes called a map because it "maps" 
#a function (in this case the method capitalize) onto each of the elements in a sequence.
#
#Exercise 2  
#Use capitalize_all to write a function named capitalize_nested that 
#takes a nested list of strings and returns a new nested list with all strings capitalized.
def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res
def capitalize_nested(listy):
	result = []
	for nest in listy:
		result.append(capitalize_all(nest))
	return result
nested_list = [['this', 'is', 'a', 'very', 'long', 'sentence'],
 ['this', 'is', 'a', 'second', 'sentence', 'in', 'a', 'different', 'list'], 
 ['lets', 'do', 'one', 'more', 'for', 'consistency', 'sake']]
print capitalize_nested(nested_list)