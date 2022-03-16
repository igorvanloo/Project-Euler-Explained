#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:54:43 2022

@author: igorvanloo
"""
'''
Project Euler Problem 

Anwser:

'''
import time, math
from functools import cache
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2*i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def k_smooth_numbers(primes, limit):
    array = [0,1] + [0] * (limit - 1)
    k_s_n = [1]
    p = primes
    new_primes = []
    while len(p) != 0:
        temp_k_s_n = []
        curr_p = p.pop(0)
        new_primes.append(curr_p)
        
        try:
            next_p = p[0]
        except IndexError:
            next_p = limit + 1
            
        power_limit = int(math.log(limit, curr_p)) + 1
        curr_multiples = [curr_p**x for x in range(1, power_limit + 1)]
        for x in curr_multiples:
            for y in k_s_n:
                temp = x*y
                if temp <= limit:
                    temp_k_s_n.append(temp)
        k_s_n += temp_k_s_n
        for x in range(curr_p, next_p):
            array[x] = len(k_s_n)
    return array, new_primes

def max_prime_factor_sieve(n):
    result = [x for x in range(n + 1)]
    result[0] = 0
    result[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if result[i] == i:
            for j in range(2*i, len(result), i):
                temp = result[j]
                while temp % i == 0:
                    temp //= i
                    
                if temp == 1:
                    result[j] = i
                else:
                    result[j] = temp
    return result

def sum_of_primes(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]

def compute(N, p):
    boolean_primes = list_primality(math.floor(math.sqrt(N)))
    
    @cache
    def mpf(N, p):
        total = sum_of_primes(N) - sum_of_primes(p-1)
        sqrt_N = math.floor(math.sqrt(N))
        primes = [i + p for (i, isprime) in enumerate(boolean_primes[p:sqrt_N + 1]) if isprime]
        for prime in primes:
            total += mpf(N//prime, prime)
        return total 
    
    return mpf(N, p) % 10**9

if __name__ == "__main__":
    print(compute(10**9, 2))
    #compute(10**7, 2) = 366736156 --- 3.0406289100646973 seconds ---
    #compute(10**8, 2) = 412898167 --- 18.694313049316406 seconds ---
    #compute(10**9, 2) = 895017934 --- 162.99369025230408 seconds ---
    print("--- %s seconds ---" % (time.time() - start_time))
