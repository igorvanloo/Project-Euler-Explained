#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:55:39 2022

@author: igorvanloo
"""

'''
Project Euler Problem 722

https://en.wikipedia.org/wiki/Lambert_series#Examples
Here we can find a simplifcation, using decimal module and a lot of time it would theoretically work
Futher research led me to below, and there is no need for a code

https://en.wikipedia.org/wiki/Divisor_function#Series_relations
Here we find sum_{n = 1 to inf} q^n * sigma_k(n) = zeta(k + 1) * sum_{n = 1 to inf} n^k * q^n

= https://www.wolframalpha.com/input/?i=zeta%2816%29 * https://www.wolframalpha.com/input/?i=%28sum+from+n+%3D+1+to+inf+n%5E15+*+%281-+1%2F2%5E25%29%5En%29

Anwser:
    3.3767927765019874495661798092357242956848214897422484015781 × 10^132
    ~ 3.376792776502 × 10^132
'''

import time, math
from decimal import *
getcontext().prec = 20
start_time = time.time()

def E(k, q):
    total = 0
    for n in range(1, 10**8):
        if n % 10**7 == 0:
            print(n)
        x = Decimal(q**n)
        total += Decimal(n**k) * x/(Decimal(1) - x)
    return total
    
if __name__ == "__main__":
    #print(E(1, 1 - Decimal(1)/Decimal(2**4))) #Good enough with 10^6
    #print(E(3, 1 - Decimal(1)/Decimal(2**8))) #Good enough with 10^7
    #print(E(7, 1 - Decimal(1)/Decimal(2**15))) #Good enough with 2*10^7
    print(E(15, 1 - Decimal(1)/Decimal(2**25)))
    print("--- %s seconds ---" % (time.time() - start_time))