# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 10:28:07 2024

@author: Igor Van Loo
"""
'''
Project Euler Problem 725

https://oeis.org/A064544

DS-number is sum of digits - i = i
that is in a number x, there is a digit d such that sum_of_digits(x) = 2i

Find partition for all numbers, for example 4 has the following partitions
4 = (1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)

This means for the partition (2, 1, 1) we want to count all n digit numbers with digits (2, 1, 1, 4)
This means there are n - 4 0's, that is there are n!/(d_0!d_1!...d_9!) where d_i = # of digit i in permutation

Then notice that suppose a digit is fixed in a position, then d_i goes down by 1, and we have 
(n - 1)!/(d_0!d_1!...(d_i - 1)!...d_9!) such numbers, if it is fixed in position k, then
this number contibutes i * 10^k * (n - 1)!/(d_0!d_1!...(d_i - 1)!d_9!) but we need need to divide by d_i, since
i can permute with others i's, in total we have i * 10^k * (n - 1)!/(d_0!d_1!...d_9!)

Hence for every partition of x we get the total sum 
= (10^n - 1)/9 * (sum_{i in x} d_i * i * (n - 1)!/(d_0!d_1!...d_9!))
= (10^n - 1)/9 * (sum_{i in x} d_i * i (n - 1)!/(d_0!d_1!...d_9!)) 
= (10^n - 1)/9 * (sum_{i in x} d_i * i) * (n - 1)!/(d_0!d_1!...d_9!)

Answer:
    4598797036650685
--- 0.05395150184631348 seconds ---
'''
import time, math
start_time = time.time()

def partition(goal):
    A = [x for x in range(1, goal + 1)]
    part = [[] for _ in range(goal + 1)]
    part[0] = [()]
    for options in A:
        for i in range(len(part) - options):
            for y in part[i]:
                part[i + options].append((options,) + y)
    return part

def combs(x, n):
    d = [x.count(i) for i in range(10)]
    d[0] = n - sum(d)
    t = math.factorial(n) // math.factorial(d[0])
    for v in range(1, 10):
        t //= math.factorial(d[v])
    return t

def S(n):
    part = partition(9)
    total = 0 
    mod = 10**16
    rep = (10**n - 1)//9
    
    for k in range(10):
        for p in part[k]:
            p += (k, )
            if len(p) - 1 < n:
                v = rep * 2*k * combs(p, n) // n
                total += v
                total %= mod
    return total

if __name__ == "__main__":
    print(S(2020))
    print("--- %s seconds ---" % (time.time() - start_time))