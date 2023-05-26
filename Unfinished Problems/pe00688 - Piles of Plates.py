# -*- coding: utf-8 -*-
"""
Created on Mon May  8 12:17:11 2023

@author: IP176077
"""
'''
Project Euler Problem 688

Brute force F(n) by hand

F(0) = 0
F(1) = 1 (1)
F(2) = 2 (2)
F(3) = 4 (3), (1, 2)
F(4) = 5 (4), (1, 3)
F(5) = 7 (5), (2, 3)
F(6) = 9 (6), (2, 4), (1, 2, 3)
F(7) = 11 (7), (3, 4), (1, 2, 4)
F(8) = 12 (8), (3, 5), (1, 3, 4)
F(9) = 15 (9), (4, 5), (2, 3, 4)
F(10) = 17 (10), (4, 6), (2, 3, 5), (1, 2, 3, 4)

This gives us https://oeis.org/A060831
Therefore F(n) = n + floor(n/3) + floor(n/5) + floor(n/7) + floor(n/9) + ...
               = n + sum_{i = 3, i is odd}^n floor(n/i)
               = sum_{i = 1, i is odd}^n floor(n/i)

S(N) = sum_{n = 1}^N F(n)
     = sum_{n = 1}^N sum_{i = 1, i is odd}^n floor(n/i)
     = 1 + 2 + (3 + floor(3/3)) + (4 + floor(4/3)) + (5 + floor(5/3) + floor(5/5)) + ...
     = 
     
Anwser:

'''
import time, math
start_time = time.time()

def F(n):
    return n + sum(n//i for i in range(3, n + 1, 2))

def S(N):
    return sum(F(n) for n in range(1, N + 1))

def compute():
    pass

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
