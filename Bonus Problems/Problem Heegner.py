# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:57:54 2025

@author: IP176077
"""
'''
Project Euler Problem 

Implemented in WolframAlpha first then did it in python using Decimal module

Answer:
    -163
--- 0.0691690444946289 seconds ---
'''
import time, math
import decimal as dc

start_time = time.time()

def is_sq(x):
    sq = (x ** (1 / 2))
    if round(sq) ** 2 == x:
        return True
    return False

def compute(N):
    m, i = 10**8, None
    dc.getcontext().prec = 50
    pi = dc.Decimal('3.1415926535897932384626433832795028841971693993751')
    
    for n in range(N + 1):
        if is_sq(n) == False:
            x = pi * dc.Decimal(n).sqrt()
            v = (dc.Decimal(x).exp() + dc.Decimal(-x).exp()) / dc.Decimal(2)
            z = math.cos(math.pi*math.sqrt(n))
            
            t1 = min(math.ceil(v) - v, v - math.floor(v))
            t2 = min(math.ceil(z) - z, z - math.floor(z))
            if t1 < m:
                m, i = t1, -n
            if t2 < m:
                m, i = t2, n
            
    return i

if __name__ == "__main__":
    print(compute(10**3))
    print("--- %s seconds ---" % (time.time() - start_time))
