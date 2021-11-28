__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list. 
#Can you make a sentence using only the letters acefhlo? Other than Hoe alfalfa? he fell off a foal
fin = open('word.txt')

def uses_only(word, letters):
	i = 0
	for char in word:
		for letter in letters:
			if char == letter:
				i = 0
				break
			else:
				i=+ 1
				continue
		if not i ==0:
			return False
		else:
			continue
	print word
	return True
for line in fin:
	word = line.strip()
	uses_only(word, 'acefhlo')