#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 11:46:44 2022

@author: igorvanloo
"""
'''
Project Euler Problem 335

First 35 values of M(n)

[1, 2, 5, 12, 15, 34, 40, 46, 53, 114, 126, 138, 152, 164, 178, 192, 207, 430, 454, 478, 506, 530, 558, 586, 616, 640, 668, 696, 726, 754, 784, 814, 845, 1722, 1770]

*2, *2 + 1, *2 + 2, + 3, *2 + 4, +6, +6, +7, *2 + 8, +12, +12, +14, +12, +14, +14, +15, *2 + 16, +24, +24, +28, +24, +28, +28, +30, +24, +28, +28, +30, +28, +30, +30, +31, *2 + 32

Clearly there is a pattern going on with powers of 2

First 10 terms of M(2**n + 1)

[2, 5, 15, 53, 207, 845, 3495, 14453, 59487, 243485]

-2**(i + 1)
[0, 1, 7, 37, 175, 781, 3367, 14197, 58975, 242461] = https://oeis.org/A005061

This sequence exactly matches 4^i - 3^i

Therefore I have that M(2^i + 1) = 2^(i + 1) - 3^i + 4^i

Sum_{k = 0}^10^18 2^(i + 1) - 3^i + 4^i = (2^(10^18 + 2) - 2) - 1/2(3^(10^18 + 1) - 1) + 1/3(4^(10^18 + 1) - 1)

Anwser:
    5032316
--- 0.00020313262939453125 seconds ---
'''
import time
start_time = time.time()

def M(n):
    array = [1]*n
    goal = [1]*n
    curr = 0
    moves = 0
    while True:
        moves += 1
        pebbles = array[curr]
        array[curr] = 0
        for x in range(pebbles):
            array[(x + curr + 1) % n] += 1
        curr = (x + curr + 1) % n
        if array == goal:
            break
    return moves

def ModDivision(a, b, m):
    try:
        inv = pow(b, -1, m)
    except ValueError:
        if a % b == 0:
            answer = (a % m * b) // b
    else:
        a = a % m
        answer = (inv * a) % m
    return answer

def compute(limit):
    mod = pow(7, 9)
    return pow(2, limit + 2, mod) - 2 - ModDivision(pow(3, limit + 1, mod) - 1, 2, mod) + ModDivision(pow(4, limit + 1, mod) - 1, 3, mod)

if __name__ == "__main__":
    print(compute(10**18))
    print("--- %s seconds ---" % (time.time() - start_time))
