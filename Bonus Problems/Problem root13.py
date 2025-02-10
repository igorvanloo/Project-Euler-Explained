# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:49:51 2025

@author: Igor Van loo
"""
'''
Project Euler Problem root13

Answer:
    4588
--- 0.0009996891021728516 seconds ---
'''
import time
import decimal as dc
start_time = time.time()

def S(n, p):
    dc.getcontext().prec = p + 5
    v = str(dc.Decimal(n).sqrt())[2:p + 2]
    return sum(int(x) for x in v)
    
if __name__ == "__main__":
    print(S(13, 1000))
    print("--- %s seconds ---" % (time.time() - start_time))
