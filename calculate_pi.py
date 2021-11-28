from __future__ import division
from decimal import Decimal

def calculate_pi(n=1000):
    """ calculate pi to n places 
    negative = False
    pi = 0
    for i in range(0, n):
        if negative:
            pi -= 4/(2*i + 1)
            negative = False
        else:
            pi += 4/(2*i + 1)
            negative = True
    
    pi = Decimal(pi)
    return pi
   
