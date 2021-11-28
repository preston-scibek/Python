__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
from math import *
def rotate_word(word, rotater):
	word = word.lower()
	new_word = ''
	for char in word:
		if ord(char) < (97 + abs(rotater)) and rotater < 0:
			num_char = 123 + (ord(char)-(97+abs(rotater)))
			num_char = chr(num_char)
			new_word += num_char
			continue
		if ord(char) + rotater > 122 and rotater > 0:
			num_char = 96 + (122-ord(char)+rotater)
			num_char = chr(num_char)
			new_word += num_char
			continue
		else:
			num_char = ord(char)
			num_char += rotater
			num_char = chr(num_char)
			new_word += num_char
			continue
	return new_word
word = raw_input("Enter word to be rotated: ")
times = input("Enter number to rotated word by: ")
print rotate_word(word, times)
