#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:59:00 2020

@author: igorvanloo
"""

'''
Porject Euler Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

x = ak*10^k +...+ a1*10^1 + a0*10^0
we need to find when ak^5 + ... + a1^5 + a0^5 = x

9^5 = 59049 therefore maximum is 9*5 * 5 = 295246 minimum is 2^5 * 2 = 64 therefore our range is 64 - 295245
'''
import math

def isfifthpower(x):
    a = str(x)
    length = len(a)
    totalsum = 0
    for i in range(0,length):
        totalsum += (int(a[i]))**5
    if totalsum == x:
        return True
    else:
        return False
    
def main():
    totalsum = 0
    for n in range(64,295246):
        if isfifthpower(n) == True:
            totalsum += n
    return totalsum
    
if __name__ == "__main__":
	print(main())

    
    


