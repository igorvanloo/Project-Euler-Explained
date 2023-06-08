# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:03:22 2023

@author: igorvanloo
"""
'''
Project Euler Problem 555

https://arxiv.org/pdf/cs/9301113v1.pdf following paper has some generalization of mccarthy 91 function

Notably theorem 1

f(x) = x - b if x > a else f^c(x + d)

Theorem 1. The generalized 91 recursion with parameters (a, b, c, d) defines a total function on
the integers if and only if (c−1) b < d. In such a case the values of f(x) also obey the much simpler
recurrence f(x) = if x > a then x − b else f(x + d − (c − 1)b)

So in our case we have M_{m, k, s}(n) = n - s if n > m else M_{m, k ,s}(M_{m, k, s}(n + k))

That is f = M_{m, k ,s}

a = m
b = s
c = 2
d = k

(c - 1)b = s < d = k, so if s < k then we have the above case which happens to always be the case (surprise!)

therefore we can simplify M_{m, k, s}(n)

Further down it shows that in the total case we actually have 

M_{m, k , s}(n) = n - s if n > m else m + k - 2s - (m - n (mod k - s))

It is clear that a fixed point must be between 0 and m

This indeed gets us the answer for S(1000, 1000)

We need to optimise SF(m, k, s)

we are looking for x = m + k - 2s - (m - x (mod k - s))
that is m - x (mod k - s) = m + k - 2s - x

I notice that if t = m + k - 2s then if M(t, m, k, s) == t then all values from t - (k - s) + 1 to t are also fixed
points note that M(t, m, k, s) == t <=> (2s - k) (mod k - s) == 0

2s - k = s (mod k - s) = 0 <=> k - s|s

So loop through s, find all divisors, d, of s, then d = k - s <=> k = d + s then we find SF(m, k, s)

note that we restrict k <= p

Anwser:
    208517717451208352
--- 6.045825481414795 seconds ---
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
            
def divisors(n, proper = False):

    pf = prime_factors(n)
    primes = [x for x in pf]
    l = len(primes)

    def gen(n = 0):
        if n == l:
            return [1]
        else:
            pows = [1]
            p = primes[n]
            for _ in range(pf[p]):
                pows.append(pows[-1] * p)
            
            div = []
            for q in gen(n + 1):
                for p in pows:
                    div.append(q * p)
            return div
                    
    div = gen()
    if proper:
        div.pop(-1)
        return div
    return div
        
def S1(p, m):
    total = 0
    for s in range(1, p):
        for d in divisors(s):
            k = d + s
            if k <= p:
                total += (d*(2*m + d - 2*s + 1))//2
    return total

def S(p, m):
    return sum(sum((d*(2*m + d - 2*s + 1))//2 for s in range(d, p - d + 1, d)) for d in range(1, p))
            
if __name__ == "__main__":
    print(S(10**6, 10**6))
    print("--- %s seconds ---" % (time.time() - start_time))
