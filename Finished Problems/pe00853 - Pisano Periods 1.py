# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:40:53 2023

@author: igorvanloo
"""
'''
Project Euler Problem 853

https://en.wikipedia.org/wiki/Pisano_period

1. π(mn) = lcm(π(m), π(n))
2. π(p^k) = π(p) * p^(k - 1)
3. if π(p)|n => p|F_n

Therefore if n = p_1^e_1 * ... * p_k^e_k then
π(n) = lcm(π(p_1^e_1), ..., π(p_k^e_k))
     = lcm(π(p_1)*p_1^(e_1 - 1), ..., π(p_k)*p_k^(e_k - 1))

1. Find prime factors of F_{120}
2. Calculate π(p) for all these prime factors 
    2.1 Keep p if π(p)|n and get multiplicty up to which π(p^e)|n
3. Generate all possible multiples of this primes up to their multiplicities 
4. sum all values such that π(n) = 120

Anwser:
    44511058204
--- 0.0 seconds ---
'''
import time, math
start_time = time.time()

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                factors[n] = 1
            break
    return factors

def fibonacci(n, m = None):

    if type(n) != int:
        return "n must be an integer"
    
    if m != None:
        f2, f1, f0 = 1, 1, 0
        for bit in bin(n)[3:]:
            v = (f1*f1) % m
            f2, f1, f0 = (f2 * f2 + v) % m, ((f2 + f0) * f1) % m, (v + f0 * f0) % m
            if bit == '1':
                f2, f1, f0 = f2 + f1, f2, f1 
    else:
        f2, f1, f0 = 1, 1, 0
        for bit in bin(n)[3:]:
            v = f1*f1
            f2, f1, f0 = f2 * f2 + v, (f2 + f0) * f1, v + f0 * f0
            if bit == '1':
                f2, f1, f0 = f2 + f1, f2, f1   
    return f1

def lcm(*numbers):  # Returns lcm of a list of numbers
    n = sorted(numbers)
    curr = n.pop(-1)
    while len(n) != 0:
        temp = n.pop(-1)
        curr = int(abs(curr * temp) / math.gcd(curr, temp))
    return curr

def pi(n, limit):
    #Find period for primes
    f_0 = 0
    f_1 = 1
    c = 0
    while True:
        f_n = (f_0 + f_1) % n
        c += 1
        if c > limit:
            break
        f_0 = f_1
        f_1 = f_n
        
        if (f_0, f_1) == (0, 1):
            break
    return c

def gen_multiples(primes, pivalues, multiplicities, limit):
    #Generates all multiples of given primes up to a cetain multiplicity
    #Extra condition to precalculate pi(n)
    p, vpi = 1, 1
    multiples = []
    for i in range(multiplicities[0] + 1):
        if p > 1:
            multiples.append((p, vpi))
            
        if len(primes) > 1:
            for (x, xpi) in gen_multiples(primes[1:], pivalues[1:], multiplicities[1:], limit//p):
                if p*x < limit:
                    multiples.append((p*x, lcm(vpi, xpi)))
        
        if i == 0:
            p *= primes[0]
            vpi *= pivalues[0]
        else:
            p *= primes[0]
            vpi *= primes[0]
    return multiples

def compute(n, limit):
    primes = []
    pivalues = []
    multiplicities = []
    for p in prime_factors(fibonacci(n)):
        vpi = pi(p, n)
        if n % vpi == 0:
            primes.append(p)
            pivalues.append(vpi)
            i = 0
            while n % vpi == 0:
                vpi *= p
                i += 1
            multiplicities.append(i)

    multiples = gen_multiples(primes, pivalues, multiplicities, limit)
    return sum(x for (x, y) in multiples if y == n)
    
if __name__ == "__main__":
    print(compute(120, 10**9))
    print("--- %s seconds ---" % (time.time() - start_time))
