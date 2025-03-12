# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:24:21 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 158

Answer:

'''
import time
from itertools import permutations
start_time = time.time()

def p(n):
    total = 0
    for string in permutations([chr(x) for x in range(97, 123)], n):
        c = 0
        for i in range(len(string) - 1):
            if ord(string[i]) < ord(string[i + 1]):
                c += 1
        if c == 1:
            total += 1 
    return total

def compute():
    return max(p(n) for n in range(1, 27))
    
if __name__ == "__main__":
    print(p(3))
    print("--- %s seconds ---" % (time.time() - start_time))
