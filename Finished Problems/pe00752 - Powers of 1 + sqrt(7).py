# -*- coding: utf-8 -*-
"""
Created on Sun May 28 11:42:19 2023

@author: igorvanloo
"""
'''
Project Euler Problem 752

(1 + sqrt(7))^n = sum_{k = 0}^n nCk sqrt(7)^(n - k)

(1 + sqrt(7))^2 = 8 + 2sqrt(7)
(1 + sqrt(7))^2 = 2C0*7 + 2C1 sqrt(7) + 2C2*1 = 8 + 2sqrt(7) 

as problem says (1 + sqrt(7))^n = a(n) + b(n)sqrt(7)

then a(n) = sum_{n - k is even}^n nCk 7^((n - k)/2)
     b(n) = sum_{n - k is odd}^n nCk 7^((n - k - 1)/2)

how do we know if there is no solution?

Using a brute force check (stop checking after 1000 cases)
the following numbers produce an outcome:
    5, 7, 11, 13, 17, 19, 23, 25, 29, 31, ... the pattern is obvious n = 6k +- 1
    except for a few values n = 61, 67, 71, 73, 89, 97, which I get by generating bigger n
    
    And no other numbers besides numbers of the form 6k +- 1 are found, this confirms my guess
    that only numbers of the form 6k +- 1 are included but i'm just not finding n fast enough
    
    I noticed that g(5) = 12, 24, 36, etc... that is every multiple of n solves the congruences
    this means if x = p*q for example 35 = 5*7 then g(35) = lcm(g(5), g(7)), not exactly sure why
    but it is helpful since every prime can be written as 6k +- 1

Next idea: inspired by https://mathlesstraveled.com/2017/07/06/the-curious-powers-of-1-sqrt-2-recurrences/

let (1 + sqrt(7))^n = (a(n) + b(n)sqrt(7))

then (1 + sqrt(7))^(n + 1) = (a(n) + b(n)sqrt(7))(1 + sqrt(7))
                           = a(n) + b(n)sqrt(7) + a(n)sqrt(7) + 7b(n)
                           = (a(n) + 7b(n)) + (a(n) + b(n))sqrt(7)

therefore a(n + 1) = a(n) + 7b(n)
          b(n + 1) = a(n) + b(n)

Upon closer inspection of a(n), b(n) 
we have a(n) = 2*a(n - 1) + 6*a(n - 2)
and b(n) = 2*b(n - 1) + 6*b(n - 2)

We want n such that a(n) = 1 (mod x), b(n) = 0 (mod x)

so why is g(3) = 0?
Well a(1) = 1 (mod 3), b(1) = 1 (mod 3)

therefore b(2) = 2 (mod 3), a(2) = 2 (mod 3) => b(3) = 1 (mod 3), a(3) = 1 (mod 3)
so it keep cycling between 1, 1 and 2, 2, so once we get into a cycle we cannot escape

this also explains the multiples since the cycle will simply repeat hence every multiple of n will solve the congruence

Anwser:
    5610899769745488
--- 233.407475233078 seconds --- with scipy divisors
--- 8.340565919876099 seconds --- with pypy
'''
import time, math
#from sympy import divisors
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

def power(mod):
    a0, a1 = 1, 1
    b0, b1 = 0, 1
    n = 2
    i = 1
    while True:
        an = (2*a1 + 6*a0) % mod
        bn = (2*b1 + 6*b0) % mod
        if bn == 0:
            print(i, n)
            i += 1
            
        if an == 1 and bn == 0:
            return n
        a0 = a1
        a1 = an
        
        b0 = b1
        b1 = bn
        
        n += 1

def quad_power(n, mod):
    #(1 + sqrt(7))^n = (a(n) + b(n)sqrt(7))
    #(1 + sqrt(7))^(n + 1) = (a(n) + 7b(n)) + (a(n) + b(n))sqrt(7)
    # => a(n + 1) = a(n) + 7b(n), b(n + 1) = a(n) + b(n)
    #(1 + sqrt(7))^(2n) = (a(n) + b(n)sqrt(7))(a(n) + b(n)sqrt(7))
    #                   = a(n)^2 + 7b(n)^2 + 2a(n)b(n)sqrt(7)
    a_res, b_res = 1, 0
    a_sq, b_sq = 1, 1
    while n != 0:
        if n % 2 == 1:
            a_res, b_res = (a_sq*a_res + 7*b_sq*b_res) % mod, (a_sq*b_res + b_sq*a_res) % mod
            n -= 1
        a_sq, b_sq = (a_sq*a_sq + 7*b_sq*b_sq) % mod, 2*a_sq*b_sq % mod
        n //= 2
    return a_res, b_res
        
def G(N):
    res = 0
    values = [0]*(N + 1)
    values[7] = 7
    for x in range(2, N + 1):
        if x % (N/10) == 0:
            print(x)
            
        if x % 6 == 1 or x % 6 == 5:
            t = 1
            pf = prime_factors(x)
            for p in pf:
                if values[p] != 0:
                    t = math.lcm(values[p]*pow(p, pf[p] - 1), t)
                else:
                    for d in divisors((p - 1)*(p + 1))[1:]:
                        if quad_power(d, x) == (1, 0):
                            values[p] = d
                            t = values[p]
                            break
            #print(x, t)
            res += t
    return res

if __name__ == "__main__":
    print(G(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))