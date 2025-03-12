# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:37:14 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 155

Extremely simple problem. For a given N just find combinations of x and N-x capacitors, which you have already computed,
in series and in parallel. Then I just add all the combinations and make sure there are not duplicates using sets,
and to ensure precision I use fractions module. Note that 60 is arbritrary, just set it to 1 for the same answer.

https://oeis.org/A153588
 
Answer:
    3857447
--- 558.0285637378693 seconds ---
--- 76.81572437286377 seconds --- Using pypy
'''
import time
from fractions import Fraction
start_time = time.time()

def D(N):
    
    C = [set([]) for _ in range(N + 1)]
    C[1].add(Fraction(1))
    
    for x in range(2, N + 1):
        print(x)
        for y in range(1, x):
            for i in C[y]:
                for j in C[x - y]:
                    C[x].add(Fraction(i) + Fraction(j))
                    C[x].add(Fraction(1/(1/i + 1/j)))
    t = set([])
    for x in range(N + 1):
        t = t.union(C[x])
    return len(t)
            

if __name__ == "__main__":
    print(D(18))
    print("--- %s seconds ---" % (time.time() - start_time))
