# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:15:58 2023

@author: igorvanloo
"""
'''
Project Euler Problem 402

Brute force calculating gets me S(10)

Now I noticed that it seems M(a, b, c) is always a divisor of 24

Calculating S(100), S(200) I again see M(a, b, c) is always a divisor of 24

Therefore M = {1, 2, 3, 4, 6, 8, 12, 24}

Anwser:

'''
import time, math
start_time = time.time()

def f(a, b, c, n):
    return pow(n, 4) + a*pow(n, 3) + b*pow(n, 2) + c*n

def M(a, b, c):
    v = math.gcd(f(a, b, c, 1), f(a, b, c, 2))
    v1 = math.gcd(v, f(a, b, c, 3))
    n = 4
    while True:
        v2 = math.gcd(v1, f(a, b, c, n))
        if v2 == v1 == v:
            break
        n += 1
        v = v1
        v1 = v2
    return v2

def S(N):
    total = 0
    Mvalues = set([])
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            for c in range(1, N + 1):
                v = M(a, b, c)
                if v == 3:
                    print(a, b, c)
                total += v
    return total, Mvalues

if __name__ == "__main__":
    print(S(20))
    print("--- %s seconds ---" % (time.time() - start_time))
