__author__ = "Preston Scibek"
# This Python file uses the following encoding: utf-8
from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001
print bob
def triangle(t, r, angle):
    y = r * sin(angle * pi / 180)
    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)
def flower(t, n, length):
	angle = 360.0/n
	for i in range(n):
		triangle(t, length, angle/2)
		lt(t,angle)
flower(bob, 7, 100)
wait_for_user()