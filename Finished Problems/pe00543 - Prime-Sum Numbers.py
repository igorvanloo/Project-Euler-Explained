# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:20:16 2023

@author: igorvanloo
"""
'''
Project Euler Problem 543

P(n, k) = 1 if n can we written as sum of k primes (can be repeated), if not P(n, k) = 0

My idea is as follows:

create a matrix such that matrix[n][k] = P(n, k)
clearly matrix[0][k] = 0, matrix[n][0] = 0

Furthermore, P(n, 1) = 1 if n is prime, 0 otherwise
Now P(n, k) = 0 if k >= n//2

now lets say we try to find P(3, 2), clearly it must include 2 is the only prime < 3
so what we're really trying to find is P(1, 1), which is 0 so P(3, 2) = 0

P(4, 2) = P(1, 1) or P(2, 1) so its true
P(4, 3) = P(1, 2) or P(2, 2) so it's false, etc, etc

I detail S(10) case

[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

total = 1 + 1 + 1 + 2 + 2 + 3 + 3 + 3 + 4 = 20 as it should be, coding this up confirms S(100) and S(1000)

But creating a matrix like this is definetly going to cause memory issues

Clearly sum(matrix[x][1] for x in range(1, n + 1)) = primepi(n) 

Also I notice that for 

n >= 6, P(n, 3) = 1 
n >= 8, P(n, 4) = 1
or in general for n >= 2x, x >= 3, P(n, x) = 1

Doesn't seem to be true for k = 2 case. I test for S(1000) and the pattern seems to be true

So for k = 1 we have sum(matrix[x][1] for x in range(1, n + 1)) = primepi(n) 

for k >= 3 we have sum(matrix[x][k] for x in range(1, n + 1)) = n + 1 - 2k

sum_{k = 3 to n//2 + 1} n + 1 - 2k = (n//2 + 1 - 3)*(n + 1) - 2*(n//2(n//2 + 1)/2 - 3)
                               = (n//2 - 2)*(n + 1) - n//2(n//2 + 1) + 6
                               
So we need to figure out the k = 2 case

goldbachs conjecture tells us every even number is the sum of 2 primes, furthermore if an odd number is 
a sum of 2 primes it means one of the primes must be 2

so for all odd numbers, x, between 3 and n if x - 2 is prime then P(x, 2) = 1

for example if n = 10 we test if 1, 3, 5, 7 are prime (3, 5, 7) are hence P((5, 7, 9), 2) = 1 

this is the same as counting all primes less than n - 2 exlcuding 2!

Anwser:
    199007746081234640
--- 2.31754732131958 seconds ---
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

def matrix_S(n):
    #This function was very useful for testing and was my inital idea
    primes = list_primes(n)
    
    matrix = []
    for x in range(n + 1):
        t = [0]*(n + 1)
        if x in primes:
            t[1] = 1
        matrix.append(t)
    
    for x in range(3, n + 1):
        for k in range(2, x//2 + 1):
            for p in primes:
                if p > x:
                    break
                if matrix[x - p][k - 1]:
                    matrix[x][k] = 1
                    break
            
    total = 0
    for x in range(n + 1):
        t = sum(matrix[x])
        #print(x, t)
        total += t
            
    return total

def primepiarray(limit):  # Returns an array such that array[x] = number of primes < x
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
    array = primepiarray(limit)
    
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

def fibonacci(n):  # Finds the nth fibonacci number
    v1, v2, v3 = 1, 1, 0  # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2

def S(n):
    res = 0
    
    #k = 1 case
    res += primePi(n)
    
    #k = 2 case
    if n >= 4:
        #all even numbers (except 2) are the sum of 2 prime
        res += n//2 - 1
        #all odd numbers - 2 which are still prime, excluding 2
        res += primePi(n - 2) - 1
                
    #k >= 3 case
    if n >= 6:
        #res += (n//2 - 2)*(n - n//2 - 2)
        res += (n//2 - 2)*(n + 1) - (n//2 + 1)*(n//2) + 6
    
    return res

def compute(k):
    total = 0
    for k in range(3, k + 1):
        fib = fibonacci(k)
        t = S(fib)
        #print(k, fib, t)
        total += t
    return total
    
if __name__ == "__main__":
    print(compute(44))
    print("--- %s seconds ---" % (time.time() - start_time))
