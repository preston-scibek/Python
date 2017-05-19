__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#Practice using the Python interpreter as a calculator:
#The volume of a sphere with radius r is 4/3 pi r3. 
#What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!
from math import *
r = 5
print "R = %d" %r
volume = (4.0/3.0) * pi * r**3
print "volume = (4.0/3.0) * pi * r**3"
print "The volume is %d." %volume
#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
price = 24.95
discount = price - (price * .4)
shipping = 0.0
sum = 0.0
for num in range(0,60):
	if num == 0:
		shipping = 3.0
	if num > 0:
		shipping = .75
	sum = sum + discount + shipping
print """
price = 24.95
discount = price - (price * .4)
shipping = 0.0
sum = 0.0
for num in range(0,60):
	if num == 0:
		shipping = 3.0
	if num > 0:
		shipping = .75
	sum = sum + discount + shipping
"""
print "The price is %d." %sum
# price = $945.45
#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, 
#what time do I get home for breakfast?
#8:05
start_hr = 6.00
start_min = (52.0)
easy_pace = 8.00 + (15.0/60.0)
tempo = 7.00 + (12.00 / 60.00)
slow = easy_pace * 2.0
fast = tempo * 3.0
run = slow + fast

print"""start_hr = 6.00
start_min = (52.0)
easy_pace = 8.00 + (15.0/60.0)
tempo = 7.00 + (12.00 / 60.00)
slow = easy_pace * 2.0
fast = tempo * 3.0
run = slow + fast
"""
print "Breakfast at %d:%f" %(7, run-8)