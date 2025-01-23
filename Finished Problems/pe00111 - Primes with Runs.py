# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:58:33 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 111

Complete brute force 

Answer:
    612407567715
--- 353.88585686683655 seconds ---
'''
import time, math, itertools
start_time = time.time()

def is_prime(x):  # Test if giving value is a prime
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True
    
def S(n, d):
    for x in range(n):
        L = set()
        for y in itertools.product([i for i in range(10)], repeat = x):
            for z in set([x for x in itertools.permutations([d]*(n - x) + list(y), n)]):
                if z[0] != 0:
                    v = int("".join([str(i) for i in z]))
                    
                    if is_prime(v):
                        L.add(v)
        if len(L) > 0:
            #print("M:", x)
            #print("N:", len(L))
            return sum(L)
                
def compute(n):
    total = 0
    for d in range(10):
        print("d:", d)
        total += S(n, d)
    return total

if __name__ == "__main__":
    print(compute(10))
    print("--- %s seconds ---" % (time.time() - start_time))
