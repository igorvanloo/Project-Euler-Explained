# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:37:19 2023

@author: igorvanloo
"""
'''
Project Euler Problem 712

D(n, m) = sum_{p is prime} |v_p(n) - v_p(m)| where v_p(n) = largest r such that p^r|n

S(N) = sum_{1 <= n, m <= N} D(n, m)

It is clear that we need to consider primes <= sqrt(n) and primes >= sqrt(n)

If a prime is >= sqrt(n) then v_p(n) is between 0 and 2

Lets exam S(10) more deeply

p = 2, 3, 5, 7

In the range [1, 10] we have floor(10/2^0) = 10 numbers divisble by 2^0
                             floor(10/2^1) = 5 numbers divisible by 2^1
                             floor(10/2^2) = 2 numbers divisble by 2^2
                             floor(10/2^3) = 1 numbers divisble by 2^3

Therefore we have floor(10/2^0) - floor(10/2^1) = 5 numbers such that v_2(n) = 0 (1, 3, 5, 7, 9)
                  floor(10/2^1) - floor(10/2^2) = 3 numbers such that v_2(n) = 1 (2, 6, 10)
                  floor(10/2^2) - floor(10/2^3) = 1 numbers such that v_2(n) = 2 (4)
                  floor(10/2^3) - floor(10/2^4) = 1 numbers such that v_2(n) = 3 (8)
                  
We can do similar things for p = 3, 5, 7

S(N) = sum_{1 <= n, m <= N} D(n, m) = sum_{1 <= n, m <= N} sum_{p <= N} |v_p(n) - v_p(m)|
     = sum_{p <= N} sum_{1 <= n, m <= N} |v_p(n) - v_p(m)|

By reorganising we can get a clearly picture

Say p = 2, now we find sum_{1 <= n, m <= N} |v_p(n) - v_p(m)|

Suppose n = 1, 3, 5, 7, 9, then we already know a lot
if m = 1, 3, 5, 7, 9 then |v_p(n) - v_p(m)| = 0
if m = 2, 6, 10 then |v_p(n) - v_p(m)| = 1
if m = 4 |v_p(n) - v_p(m)| = 2
if m = 8 |v_p(n) - v_p(m)| = 3

therefore we have 5*5*0 + 5*3*1 + 5*1*2 + 5*1*3 = 15 + 10 + 15 = 40

if n = 2, 6, 10
if m = 4 then |v_p(n) - v_p(m)| = 1
if m = 8 then |v_p(n) - v_p(m)| = 2

we have 3*1*1 + 3*1*2 = 9

if n = 4
if m = 8 then |v_p(n) - v_p(m)| = 1

we have 1*1*1 = 1

In total we have 40 + 9 + 1 = 50
We multiply by 2 because we can switch m, n, hence sum_{1 <= n, m <= N} |v_2(n) - v_2(m)| = 100

Then we can repeat for other primes

Now an algorithm:
    for each p <= N:
        build a list exp such that exp[i] = number of numbers n <= N such that v_p(n) = i
        then for i in range(len(exp)):
            for j in range(len(exp)):
                add exp[i]*exp[j]*(j - i) #(j - i) represents v_p(j) - v_p(i)
    return total * 2

This works well for up to 10**8

Now we need a faster method. This method works perfectly for primes < sqrt(N)
so we need to focus on a method for primes >= sqrt(N)

for example in S(10), sqrt(10) = 3.1 so p >= sqrt(10) are 5 and 7, lets investigate

p = 5
floor(10/5^0) - floor(10/5^1) = 8 numbers such that v_2(n) = 0 (1, 2, 3, 4, 6, 7, 8, 9)
floor(10/5^1) - floor(10/5^2) = 2 numbers such that v_2(n) = 1 (5, 10)

n = 1, 2, 3, 4, 6, 7, 8, 9
m = 5, 10

Therefore we have 8*2*1 = 16

p = 7
floor(10/7^0) - floor(10/7^1) = 9 numbers such that v_2(n) = 0 (1, 2, 3, 4, 5, 6, 8, 9, 10)
floor(10/7^1) - floor(10/7^2) = 1 numbers such that v_2(n) = 1 (7)

n = 1, 2, 3, 4, 5, 6, 8, 9, 10
m = 7

Therefore we have 9*1*1 = 9

The difference between 5 and 7 is that floor(10/5) = 2

We can use the prime counting function for this.
pi(N) - pi(N/2) tells us how many primes there are less or equal to N but greater than N/2
For every prime greater than N/2 we know that floor(N/p^0) - floor(N/p^1) = N - 1 and
floor(N/p^1) - floor(N/p^2) = 1

Now are only interested in primes > sqrt(N) so we must continue till pi(N/sqrt(N))

for example for N = 10, we know sqrt(10) = 3.1
so we have pi(10) - pi(5) = 1 (7), this contribution is 1*9*1
then pi(5) - pi(3) = 1 (5), this contribution is 1*8*2

Anwser:
    413876461
--- 564.5953602790833 seconds ---
'''
import time, math
from functools import cache
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

def bisect(alist, goal):
    #Equivalent to bisect_right from bisect module
    lo = 0
    hi = len(alist)
    while lo < hi:
        mid = (lo + hi)//2
        if goal < alist[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def primepi(limit):  # Returns an array such that array[x] = number of primes < x
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

def primePi(x):
    limit = int(math.sqrt(x))
    primes = list_primes(limit)
    array = primepi(limit)
    
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
    
    return int(pi(x))

def primePiMLArray(x):
    limit = int(math.sqrt(x))
    primes = list_primes(limit)
    array = primepi(limit)
    
    @cache
    def phi(x, a):
        if a == 0:
            return int(x)
        if a == 1:
            return int(x) - x//2
        result = phi(x, a - 1) - phi(x // primes[a - 1], a - 1)
        return int(result)
    
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
    
    results = []
    for i in range(int(math.sqrt(x)), 0, -1):
        #print(i, int(math.sqrt(x)))
        results.append(pi(x/i))
        
    return results[::-1]

def S(N):
    primes = list_primes(int(math.sqrt(N)))
    total = 0
    mod = 10**9 + 7
    
    for p in primes:
        exp = []
        k = 0
        while True:
            t = N//pow(p, k) - N//pow(p, k + 1)
            if t == 0:
                break
            else:
                exp.append(t)
            k += 1
        
        for i in range(len(exp)):
            for j in range(i + 1, len(exp)):
                total += exp[i]*exp[j]*(j - i)
    
    array = primePiMLArray(N)
    for i in range(1, int(math.sqrt(N))):
        total += (array[i - 1] - array[i])*i*(N - i)
        
    return 2*total % mod

if __name__ == "__main__":
    print(S(10**12))
    print("--- %s seconds ---" % (time.time() - start_time))
