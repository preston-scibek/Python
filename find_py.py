from __future__ import division
def find_pi(places=1000):
    from decimal import Decimal
    neg = False
    pi = 0
    for i in range(0, places):
        if(neg):
            pi -= 4/(2*i + 1)
            neg = False
        else:
            pi += 4/(2*i + 1)
            neg = True
        #print pi
    pi = Decimal(pi)
    return pi