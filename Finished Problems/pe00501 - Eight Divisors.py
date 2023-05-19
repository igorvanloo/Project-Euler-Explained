# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:55:38 2023

@author: igorvanloo
"""
'''
Project Euler Problem 501

Frome divisor function we know if n = p_1^e_1...
then the number of divisors of n is (e_1 + 1)(e_2 + 1)...

Therefore if number of divisors is 8 then there are only 3 scenarios

1. n = p^7 => d(n) = (7 + 1) = 8
2. n = p_1^3p_2 => d(n) = (3 + 1)(1 + 1) = 8
3. n = p_1p_2p_3 => d(n) = (1 + 1)(1 + 1)(1 + 1) = 8

seeing as p_1p_2p_3 < p_3^3 we only need to generate primes up till the cube root of N

Now lets go case by case:
    pi(n) = prime counting function
    
    1. Find biggest prime, p < N^(1/7) there will be pi(p) numbers with 8 divisors
    
    2. p_1 < (N/2)^(1/3), now if p_1 < n/p1^3 then there will be pi(n/p1^3) - 1 numbers with 8 divisors
        otherwise there will be pi(n/p1^3) numbers with 8 divisors
        
    3. Assume p_1 < p_2 < p_3, then p_3 < N/(2*3) go through p1 and p2 then there will be 
        pi(n/(p1p2)) - pi(p2) numbers with 8 divisors

Anwser:
    197912312715
--- 241.3640172481537 seconds ---
'''
import time, math
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def primepi_array(limit):  # Returns an array such that array[x] = number of primes < x
    prime_gen = list_primality(limit + 50)
    primes = [x for x in range(len(prime_gen)) if prime_gen[x]]
    array = [0] * (limit + 1)
    p_index = 0
    for x in range(1, limit + 1):
        while True:
            if primes[p_index] > x:
                array[x] = p_index
                break
            p_index += 1
    return array

def f(n):
    limit = int(math.sqrt(n))
    primes = list_primes(limit)
    array = primepi_array(limit)
    
    phiCache = {}
    def phi(x, a):
        if (x, a) in phiCache:
            return phiCache[(x, a)]
        if a == 0:
            return int(x)
        if a == 1:
            return int(x) - x//2
        result = phi(x, a - 1) - phi(int(x / primes[a - 1]), a - 1)
        phiCache[(x, a)] = result
        return result
    
    piCache = {}
    def pi(x):
        if int(x) in piCache:
            return piCache[int(x)]
        
        if x <= limit:
            return array[math.floor(x)]
        
        a = pi(pow(x, 1/4))
        b = pi(pow(x, 1/2))
        c = pi(pow(x, 1/3))
        result = phi(int(x), int(a)) + ((b + a - 2) * (b - a + 1))//2
        for i in range(a + 1, b + 1):
            w = x / primes[i - 1]
            result -= pi(w)
            if i <= c:
                bi = pi(int(math.sqrt(w)))
                for j in range(i, bi + 1):
                    result -= (pi(w / primes[j - 1]) - j + 1)
        piCache[int(x)] = result
        return int(result)
    
    total = pi(int(pow(n, 1/7)))
    
    print(total)
        
    for p1 in primes:
        p = pow(p1, 3)
        if 2*p > n:
            break
        t = pi(n/p)
        if p1 <= n//p:
            total += t - 1
        else:
            total += t
    print(total)    
    
    for i in range(len(primes)):
        p1 = primes[i]
        if pow(p1, 3) > n:
            break
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            t = n/(p1*p2)
            t1 = pi(t)
            if t > p2:
                total += t1 - (j + 1) #j + 1 is the index of the primes, equivalent to pi(p2)
            else:
                break
    return total

if __name__ == "__main__":
    print(f(10**12))
    print("--- %s seconds ---" % (time.time() - start_time))
