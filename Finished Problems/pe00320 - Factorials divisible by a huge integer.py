#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 23:04:41 2022

@author: igorvanloo
"""

'''
Project Euler Problem 320

if (i!)^1234567890 divides n!
We can use legendres formula to find how many times a prime occurs in n! using legendres formula, say e,
then we can perform a bisection algorithm to find the smallest factorial such that there are e*1234567890 factors 
of i in its factorial

Anwser:
    278157919195482643
--- 1374.538467168808 seconds ---
--- 40.60763955116272 seconds --- with pypy
'''
import time, math
start_time = time.time()

def prime_factors_sieve(limit):
    result = [{} for _ in range(limit + 1)]
    for i in range(2, limit + 1):
        if len(result[i]) == 0:
            #prime number found
            for j in range(i, limit + 1, i):
                n = j
                if i in result[j]:
                    while n % i == 0:
                        n //= i
                        result[j][i] += 1
                else:
                    result[j][i] = 1
                    n //= i
                    while n % i == 0:
                        n //= i
                        result[j][i] += 1
    return result

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                if d in factors:
                    factors[n] += 1
                else:
                    factors[n] = 1
            break
    return factors

def legendre_factorial(n, p):
    #Modified legendre factorial function, finds number of factors of p in n!
    total = 0
    for i in range(1, int(math.floor(math.log(n, p))) + 1):
        total += n // (p ** i)
    return total

def inv_legendre_factorial(p, e):
    #Finds smallest number, n, such that p^e divides n!
    #Use bisection method
    low = p #Low guess is n = p
    high = p*e #high guess is n = p*e
    while high - low > 1:
        mid = (low + high)//2
        if legendre_factorial(mid, p) >= e:
            #If middle number has more factors of p than needed
            #make high = mid
            high = mid
        else:
            #Otherwise low = mid
            low = mid
    #After high and low are one integer apart we test high and low
    if legendre_factorial(low, p) >= e:
        #If low has enough prime factors, we return low
        return low
    else:
        #Otherwise return high
        return high
    
def compute(limit):
    exp = 1234567890
    mod = 10**18
    S = 0
    
    pf = prime_factors_sieve(limit)
    curr_pf = {2:7, 3:4, 5:1, 7:1}
    
    curr_N = 9876543138
    
    for n in range(10, limit + 1):
        new_pf = pf[n]
        for p in new_pf:
            if p in curr_pf:
                curr_pf[p] += new_pf[p]
                t = inv_legendre_factorial(p, curr_pf[p]*exp)
                if t > curr_N:
                    curr_N = t
            else:
                curr_pf[p] = new_pf[p]
                t = inv_legendre_factorial(p, curr_pf[p]*exp)
                if t > curr_N:
                    curr_N = t
        S += curr_N
        S %= mod
    return S % mod
        
if __name__ == "__main__":
    print(compute(1000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    
