#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 22:19:53 2021

@author: igorvanloo
"""

'''
Project Euler Problem 675

https://en.wikipedia.org/wiki/Prime_omega_function

We have sum_{r|n} 2^ω(r) = d(n^2)

F(n) = sum_{i = 2 to n} S(i!)

and we have S(n) = d(n^2)
and we have d(n) = (e_1 + 1)(e_2 + 1)... where n = p_1^e_1 * p_2^e_2*...

S(2!) = d(4) = (2 + 1) = 3
S(3!) = d(36) = ((2*3)^2) = 2^2 * 3^2 = (3*3) = 9
S(4!) = d((2^3 * 3)^2) = d(2^6 * 3^2) = (7*3) = 21
S(5!) = d((2^3 * 3 * 5)^2) = d(2^6 * 3^2 * 5^2) = (7*3*3) = 63
S(6!) = d((2^4 * 3^2 * 5)^2) = d(2^8 * 3^4 * 5^2) = (9*5*3) = 135

We can calculate S((i+1)!) from S(i!)
if v_p(i) = x and v_p(i+1) = y where v_p(j) is the number of times prime factor p is in j, then
S((i+1)!) = S(i!) * y/x for all p < i + 1

Using a sieve to find all prime factors and modular division, problem can be solved in reasonable time

Anwser:
    416146418
--- 135.02284979820251 seconds ---
'''

import time, math
start_time = time.time()

def sieve_factors(n):
    result = [0]*(n+1)
    for i in range(2, n + 1):
        if (result[i]) == 0:
            result[i] = [[i], [1]]
            for j in range(2*i, len(result), i):
                if result[j] == 0:
                    result[j] = [[i], []]
                else:
                    result[j][0].append(i)
                temp = j
                count = 0
                while temp % i == 0:
                    count += 1
                    temp /= i
                result[j][1].append(count)
    return result

def ModDivision(a,b,m):
    a = a % m
    inv = pow(b,-1,m)
    if(inv == -1):
        return "Division not defined"
    else:
        return (inv*a) % m
    
def F(n, mod):
    main_total = 3
    running_total = 3
    sieve = sieve_factors(n)
    print("Sieve Generated")
    
    store = {2:1}
    count = 1
    
    for i in range(3, n + 1):
        if i % (count*100000) == 0:
            print(i)
            count += 1
            
        if sieve[i] == [[i], [1]]:
            running_total *= 3
            store[i] = 1
        else:
            fac, exp = sieve[i]
            
            for x in range(len(fac)):
                y = fac[x]
                running_total = ModDivision(running_total*(2*(store[y]+exp[x]) + 1), 2*store[y] + 1, mod)
                store[y] += exp[x]
            
        main_total += running_total
        main_total %= mod
    
    return main_total
    
if __name__ == "__main__":
    print(F(10**7, 1000000087))
    print("--- %s seconds ---" % (time.time() - start_time))