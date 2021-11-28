__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Modify the program to fix this error.
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		print letter + 'u' + suffix
	else:
		print letter + suffix