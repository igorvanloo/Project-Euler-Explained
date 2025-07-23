# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 11:35:29 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 209

We want to find all functions T such that T(a, b, c, d, e, f) & T(b, c, d, e, f, a ^ (b & c)) = 0

In general for n variables we have 2^n possible inputs, and for each input T( ... ) = 0 or 1, hence in total we have 2^(2^n) functions T

But in our case note that if T(a, b, c, d, e, f) = 1, it must be that T(b, c, d, e, f, a ^ (b & c)) = 0 and since we can determine the input of the second half
from the first, we will create cycles with restricted outputs limiting out possible T.

Now to find all possible T simply go through a cycle and see what values we can assign, if T(a, b, c, d, e, f) = 0, then T(b, c, d, e, f, a ^ (b & c)) can be 0 or 1
and if T(a, b, c, d, e, f) = 1, then T(b, c, d, e, f, a ^ (b & c)) = 0. COmputing small values yeilds the Lucas numbers, and since L(n) = F(n + 1) + F(n - 1)
we can compute this ultra fast

Answer:
    15964587728784
--- 0.001004934310913086 seconds ---
'''
import time
start_time = time.time()

def find_next(curr):
    t = bin(curr)[2:][::-1]
    b = [int(x) for x in t + '0'*(6 - len(t))]
    
    nb = b[1:] + [b[0] ^ (b[1] & b[2])]
    snb = ''.join([str(x) for x in nb])
    curr = int(snb[::-1], 2)
    return curr

def lucas(n):  # Finds the nth fibonacci number
    #http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/fastexp.pdf see algorithm 3
    f2, f1, f0 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for bit in bin(n)[3:]:
        v = f1*f1
        f2, f1, f0 = f2 * f2 + v, (f2 + f0) * f1, v + f0 * f0
        if bit == '1':
            f2, f1, f0 = f2 + f1, f2, f1   
    return f2 + f0

def compute():
    pointer = [None] * 64
    total = 1
    while None in pointer:
        for start, x in enumerate(pointer):
            if x == None:
                break
            
        curr = find_next(start)
        pointer[start] = curr
        cycle = (start, curr)
        while curr != start:
            t = find_next(curr)
            cycle += (t, )
            pointer[curr] = t
            curr = t
        
        total *= lucas(len(cycle) - 1)
    
    return total

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
