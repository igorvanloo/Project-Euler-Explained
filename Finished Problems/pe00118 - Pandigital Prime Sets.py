# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:47:31 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 118

Generate n-digit primes using at most one of each digit using itertools

Then given a partition of 9, I brute force check all possibilities.

Inspired once again by backtracking solution of Sudoku problem!

Answer:
    44680
--- 14.096630334854126 seconds ---
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
    
def partition(x, L, show = True):
    if 0 in L:
        return "0 cannot be part of L"
    A = [0] * (x + 1)
    A[0] = 1
    P = [[] for _ in range(x + 1)]
    P[0] = [()]
    for y in L:
        for i in range(len(P) - y):
            if show:
                for z in P[i]:
                    P[i + y].append((y,) + z)
            else:
                A[i + y] += A[i]
    if show:
        return P[-1]
    else:
        return A[-1]

def solve(part, j, S, S_set, S_all_sets, P):
    if j == len(part):
        S_all_sets.append(S_set)
        return S_set
    for x in P[part[j]]:
        if all(S[int(i)] + 1 != 2 for i in str(x)):
            SS = [S[k] for k in range(10)]
            for i in str(x):
                SS[int(i)] += 1
            if x == max(S_set + [x]):
                solve(part, j + 1, SS, S_set + [x], S_all_sets, P)

def compute():
    P = [[] for _ in range(10)]

    for k in range(1, 10):
        for x in itertools.permutations("123456789", k):
            v = int("".join(x))
            if is_prime(v):
                P[k].append(v)
        
    total = 0
    for part in partition(9, [1,2,3,4,5,6,7,8,9]):
        
        S_all_set = []
        S = [1,0,0,0,0,0,0,0,0,0]
        solve(part[::-1], 0, S, [], S_all_set, P)
        print(part, len(S_all_set))
        total += len(S_all_set)
                
    return total

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
