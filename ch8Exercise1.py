__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Write a function that takes a string as an argument and displays the letters backward, one per line
def back_string(word):
	for char, indice in enumerate(word):
		print word[0-(char+1)]
word = raw_input("Enter word to be backworded: ")
back_string(word)