#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:41:14 2020

@author: igorvanloo
"""

'''
Project euler problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

answer:
    
    [[16, 64], [19, 95], [26, 65], [49, 98]]
100.0
--- 0.0027740001678466797 seconds ---
'''

import time, math
start_time = time.time()

def compute():
    values = []
    numer = 1
    denom = 1
    for x in range(10,100):
        for y in range(x+1, 100):
            if x%10 != 0 and y%10 != 0:
                value1 = str(x)
                value2 = str(y)
                for a in value1:
                    for b in value2:
                        if a == b:
                            x1 = int(value1.replace(a,"",1))
                            y1 = int(value2.replace(b,"",1))
                            if x/y == x1/y1:
                                numer *= x1
                                denom *= y1
                                values.append([x,y])
    print(values)
    return denom/math.gcd(denom,numer)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))