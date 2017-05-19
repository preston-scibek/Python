__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#This question is based on a Puzzler that was broadcast on the radio program Car Talk:
#Give me a word with three consecutive double letters. 
#I'll give you a couple of words that almost qualify, but don't. 
#For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great
# except for the 'i' that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i.
# If you could take out those i's it would work. But there is a word that has 
#three consecutive pairs of letters and to the best of my knowledge this may be the 
#only word. Of course there
# are probably 500 more but I can only think of one. What is the word?
def solve_the_puzzle(word):
	index = 0
	trips = 0
	while index < (len(word)-1):
		if word[index] == word[index+1]:
			trips +=1
			index +=2
		elif trips >= 3:
			print word
			return word
		else:
			trips = 0
			index +=1
		
fin = open('word.txt')
for line in fin:
	word = line.strip()
	solve_the_puzzle(word)