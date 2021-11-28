__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#A palindrome is a word that is spelled the same backward and forward, like "noon" and "redivider".
# Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.
#The following are functions that take a string argument and return the first, last, and middle letters:

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]
#We'll see how they work in Chapter 8.
#Type these functions into a file named palindrome.py and test them out.
# What happens if you call middle with a string with two letters? One letter?
# What about the empty string, which is written '' #and contains no letters?
#Write a function called is_palindrome that takes a string argument 
#and returns True if it is a palindrome and False otherwise. 
#Remember that you can use the built-in function len to check the length of a string.
def what_happens():
	print "It = " + middle("it") # returns empty string
	print "\n"
	print "I = " + middle("I") # returns empty string
	print "\n"
	print "'' = " + middle('') # returns empty string

def is_palindrome(word):
	word = word.lower()
	x = len(word)
	new_word = last(word)
	new_fake_word = first(word) + middle(word)
	for letter in range(x-1):
		new_word += last(new_fake_word)
		new_fake_word = first(new_fake_word) + middle(new_fake_word)
	if new_word == word:
		return True
	else:
		return False
word = raw_input("What is your word: ")
print is_palindrome(word)