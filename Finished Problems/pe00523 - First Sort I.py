# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:41:32 2023

@author: igorvanloo
"""
'''
Project Euler Problem 523

Generate all possible permutations of [1, 2, ..., n] get values

E(2) = 0.5 | steps = 1 | perms = 2
E(3) = 1.5 | steps = 9 | perms = 6
E(4) = 3.25 | steps = 78 | perms = 24
E(5) = 6.25 | steps = 750 | perms = 120
E(6) = 11.416666666666666 | steps = 8220 | perms = 720
E(7) = 20.416666666666668 | steps = 102900 | perms = 5040
E(8) = 36.291666666666664 | steps = 1463280 | perms = 40320
E(9) = 64.625 | steps = 23451120 | perms = 362880

Simplifying the fractions we have:
E(2) = 1/2
E(3) = 3/2
E(4) = 13/4
E(5) = 25/4
E(6) = 137/12
E(7) = 245/12
E(8) = 871/24
E(9) = 517/8
E(10) = 4629/40

I tried searching numerator in oeis and somehow it existed: https://oeis.org/A330718 
and the denominator is https://oeis.org/A330719

This directly gave us a solution

E(n) = sum_{k = 1 to n} (2^(k - 1) - 1)/k

See website for the actual proof of why

Anwser:
    37125450.44
--- 0.0 seconds ---
'''
import time
from itertools import permutations
start_time = time.time()

def first_sort(L):
    steps = 0
    l = len(L)
    S = sorted(L)
    while True:
        if L == S:
            break
        for x in range(l - 1):
            if L[x] > L[x + 1]:
                v = L.pop(x + 1)
                L = [v] + L
                steps += 1
                break
    return steps
            
def brute_E(n):
    perms = [list(x) for x in permutations([x for x in range(1, n + 1)])]
    total = 0
    for x in perms:
        total += first_sort(x)
    return total/len(perms), total, len(perms)
        
def E(n):
    return sum((pow(2, k - 1) - 1)/k for k in range(1, n + 1))

if __name__ == "__main__":
    print(round(E(30), 2))
    print("--- %s seconds ---" % (time.time() - start_time))
