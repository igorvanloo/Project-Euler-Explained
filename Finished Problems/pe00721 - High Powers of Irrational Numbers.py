# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:42:27 2023

@author: igorvanloo
"""
'''
Project Euler Problem 721

Similar to problem 752, 318

let x = ceil(sqrt(a))
(x + sqrt(a))^n = (a(n) + b(n)sqrt(a))

(x + sqrt(a))^0 = 1           => a(0) = 1, b(0) = 0
(x + sqrt(a))^1 = x + sqrt(a) => a(0) = x, b(0) = 1

(x + sqrt(a))^(n + 1) = ((a(n) + b(n)sqrt(a)))(x + sqrt(a))
                      = (xa(n) + ab(n)) + (a(n) + xb(n))sqrt(a)
 => a(n + 1) = xa(n) + ab(n), b(n + 1) = a(n) + xb(n)

(x + sqrt(a))^(2n) = (a(n) + b(n)sqrt(a))(a(n) + b(n)sqrt(a))
                   = a(n)^2 + ab(n)^2 + 2a(n)b(n)sqrt(a)

Anwser:
    700792959
--- 127.4873640537262 seconds ---
'''
import time, math
start_time = time.time()
    
def brute_f(a, n):
    return math.floor(pow(math.ceil(math.sqrt(a)) + math.sqrt(a), n))

def f(a, n):
    total = -1
    ca = math.ceil(math.sqrt(a))
    for k in range(n//2 + 1):
        t = 2*math.comb(n, 2*k)*pow(ca, n - 2*k)*pow(a, k)
        #print(k, t)
        total += t
    return total

def bin_exp(x, a, n, mod):
    a_sq, b_sq = x, 1
    for bit in bin(n)[3:]:
        a_sq, b_sq = (a_sq*a_sq + a*b_sq*b_sq) % mod, 2*a_sq*b_sq % mod
        if bit == "1":
            a_sq, b_sq = (x*a_sq + a*b_sq) % mod, (a_sq + x*b_sq) % mod
    return a_sq, b_sq

def G(n):
    mod = 999999937
    total = 0
    for a in range(1, n + 1):
        ca = int(math.sqrt(a))
        if ca*ca == a:
            total += 2*bin_exp(ca, a, a*a, mod)[0]
        else:
            total += 2*bin_exp(ca + 1, a, a*a, mod)[0] - 1
        total %= mod
    return total

if __name__ == "__main__":
    print(G(5*10**6))
    print("--- %s seconds ---" % (time.time() - start_time))
