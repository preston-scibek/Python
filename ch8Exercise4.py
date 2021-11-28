__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Modify find so that it has a third parameter, the index in word where it should start looking
def find(word, letter, index_look):
    index = index_look
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
word = raw_input("Enter word to be searched:")
letter = raw_input("Enter letter to search for:")
index = input("Ender index where should start looking: ")
print find(word, letter, index)