__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
#The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch curve with length x, all you have to do is
#Draw a Koch curve with length x/3.
#Turn left 60 degrees.
#Draw a Koch curve with length x/3.
#Turn right 120 degrees.
#Draw a Koch curve with length x/3.
#Turn left 60 degrees.
#Draw a Koch curve with length x/3.
#The exception is if x is less than 3: in that case, you can just draw a straight line with length x.
#Write a function called koch that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch curve with the given length.
#Write a function called snowflake that draws three Koch curves to make the outline of a snowflake.
#The Koch curve can be generalized in several ways. See http://en.wikipedia.org/wiki/Koch_snowflake for examples and implement your favorite.
from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
def koch_curve(t, length):
	bob.delay = 0.0000000000000000001
	if length<3:
		fd(t, length)
		return
	m = length/3.0
	koch_curve(t, m)
	lt(t, 60)
	koch_curve(t, m)
	rt(t, 120)
	koch_curve(t, m)
	lt(t, 60)
	koch_curve(t, m)
def better_koch_curve(t, length, angle):
	bob.delay = 0.0000000001
	if length<3:
		fd(t, length)
		return
	m = length/3.0
	better_koch_curve(t, m, angle)
	lt(t, angle)
	better_koch_curve(t, m, angle)
	rt(t, angle*2)
	better_koch_curve(t, m, angle)
	lt(t, angle)
	better_koch_curve(t, m, angle)

def snowflake(t, length):
	for i in range(3):
		better_koch_curve(t, length, 60)
		rt(t, 120)
better_koch_curve(bob, 100, 85)
#snowflake(bob, 300)
wait_for_user()