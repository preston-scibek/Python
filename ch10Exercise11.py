__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Exercise 11  
#To check whether a word is in the word list, you could use the in operator,
# but it would be slow because it searches through the words in order.
#Because the words are in alphabetical order, we can speed things up with a bisection search
# (also known as binary search), which is similar to what you do when you look a word up in the dictionary. 
#You start in the middle and check to see whether the word you are looking for comes 
#before the word in the middle of the list. If so, then you search the 
#first half of the list the same way. Otherwise you search the second half.

#Either way, you cut the remaining search space in half. If the word list has 113,809 words,
# it will take about 17 steps to find the word or conclude that it's not there.
#
#Write a function called bisect that takes a sorted list and a target value and 
#returns the index of the value in the list, if it's there, or None if it's not.
#
#Or you could read the documentation of the bisect module and use that!
def bisect(listy, word):
	start = 0
	end = len(listy)-1
	while start < end:
		bisected = (start+end)/2
		if listy[bisected] < word:
			start = bisected + 1
		else:
			end = bisected
	return start	
	
listy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fin = open('word.txt')
listo = []
for line in fin:
	listo.append(line.strip())
word = raw_input("Enter word to be searched: ")
print bisect(listo,word)