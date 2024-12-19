# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:22:50 2024

@author: Igor Van Loo
"""
'''
Project Euler Problem 872

After drawing a few trees a few patterns emerge. For example the height of the tree is log_2(n) + 1
The children of node n are always [n-1, n-2, n-4, n-8, n-16, etc]
the children of n-1 are always [n-3, n-5, n-9, etc]

Essentially there is a pattern relating to 2^n.

Once you ask yourself the question: What is the parent of node x, then answer becomes clear.

From observation we have that:
    If y is the parent of x, then y - x = 2^k, where k is the largest such that x + 2^k <= n.
    If x = n, it has no parents
    
Call this property **

Proof by induction
1. Base case: Trivial
2. IH: Suppose for T_{n - 1} ** holds for all x
3. Take T_n. The longest path of T_{n - 1} is always [n-1, n-2, n-4, n-8, etc] now let x be a random node
of T_n, if x in [n-1, n-2, n-4, n-8, etc], it's parent is n, which obeys ** otherwise it's parent doesn't 
change, that is if x + 2k = y, k is as large as possible such that x + 2^k <= n + 1, then the same
k is chosen so that x + 2^k <= n

Answer:
    2903144925319290239
--- 0.0 seconds ---
'''
    
import time, math
start_time = time.time()

def f(n, x):
    total = x
    curr = x
    while curr != n:
        k = int(math.log(n - curr, 2))
        curr += pow(2, k)
        total += curr
    return total

if __name__ == "__main__":
    print(f(10**17, 9**17))
    print("--- %s seconds ---" % (time.time() - start_time))
