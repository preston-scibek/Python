__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Encapsulate this code in a function named count, 
#and generalize it so that it accepts the string and the letter as arguments.
def count(string, letter_find):
	word = string
	count = 0
	for letter in word:
		if letter == letter_find:
			count = count + 1
	print count
word = raw_input("Enter string to be searched: ")
letter = raw_input("Enter letter to be found" "")
count(word, letter)