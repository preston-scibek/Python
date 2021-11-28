__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Write a function named uses_all that takes a word and a string of
# required letters, and that returns True if the word uses all the
# required letters at least once. How many words are there that
# use all the vowels aeiou? .525442% How about aeiouy? .036904%
def uses_all(word, letters):
	used = 0
	for letter in letters:
		used = 0
		for char in word:
			if char == letter:
				used = 1
				break
			else:
				used = 0
				continue
		if used == 0:
			return False
	print word
	return True
x = 0.0
z = 0.0
fin = open('word.txt')
for line in fin:
	word = line.strip()
	if uses_all(word, 'aeiouy'):
		x += 1.0
	z+= 1.0
print "%f %% words use the given letters(%s)" %((x/z)*100.0, 'aeiouy')