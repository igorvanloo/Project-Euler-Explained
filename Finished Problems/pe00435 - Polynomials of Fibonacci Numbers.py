#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:58:29 2022

@author: igorvanloo
"""

'''
Project Euler Problem 435

F_n(x) = (f_{n+1}x^{n+1} + f_nx^{n+2} - x)/(x^2 + x - 1)

Modified my Fibonacci function to include mods to find f_10**15 quickly
Then notice that (x^2 + x - 1) | (f_{n+1}x^{n+1} + f_nx^{n+2} - x) because the solutions to F_n(x) is an integer
therefore we can use the property if a mod b = 0 => a/b mod m = (a mod m*b)/b

Proof:

a/b = x (mod m) <=> a/b = my + x< => a = bx + bmy <=> a = bx (mod bm)

Anwser:
    252541322550
--- 0.042450904846191406 seconds ---
'''

import time, math
start_time = time.time()
    
def fibonnaci_mod(n, mod): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    count = 0
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = pow(v2, 2, mod)
        v1, v2, v3 = (pow(v1, 2, mod)+calc) % mod, ((v1+v3)*v2) % mod, (calc+pow(v3, 2, mod)) % mod
        if rec=='1':
            v1, v2, v3 = v1+v2 % mod, v1 % mod, v2 % mod
        count += 1
    return v2 % mod

def F(n, x, mod):
    den = (x*x + x - 1)
    fn = fibonnaci_mod(n, mod*den)
    fn1 = fibonnaci_mod(n+1, mod*den)
    num = (fn*pow(x, n+2, mod*den) + fn1*pow(x, n+1, mod*den) - x) % (mod*den)
    return num//den
    
def compute(n, limit, mod):
    total = 0
    for x in range(limit + 1):
        total += F(n, x, mod)
    return total % mod
    
if __name__ == "__main__":
    mod = math.factorial(15)
    print(compute(10**15, 100, mod))
    print("--- %s seconds ---" % (time.time() - start_time))