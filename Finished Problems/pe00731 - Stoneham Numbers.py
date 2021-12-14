#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 00:46:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 731

A = sum_{i=1}^inf 1/(3^i * 10^(3^i))

A(n) = 10 digits after n-th position

therefore if 3^k > n => 3^k * 10^(3^k) > n*10^n therefore we no longer have to sum terms past this

We have S = sum_{i=1 to k} 1/(3^i * 10^(3^i))
We are looking for the 10 digits after this

We can multiply the whole thing by 10^{n-1}

Therefore we have S_1 = sum_{i=1 to k} 10^(n - 3^i - 1)/3^i

and we want the fractional part of what remains

But 10^(n - 3^i - 1) is massive so instead we calculate 10^(n - 3^i - 1) mod 3^i
We can do this because we have r = 10^(n - 3^i - 1)/3^i - 10^(n - 3^i - 1)//3^i = (10^(n - 3^i - 1) - 3^i*(10^(n - 3^i - 1)//3^i))/3^i
= (10^(n - 3^i - 1) mod 3^i) / 3^i

Anwser:
    0.6086371427
--- 0.0004830360412597656 seconds ---
'''

import time, math
start_time = time.time()

def compute(n):
    limit = int(math.log(n,3))
    total = 0
    for i in range(1, limit + 1):
        div = 3**i
        exp = n - div - 1
        temp = pow(10,exp,div)
        total += temp/div
    return str((total) - (math.floor(total)))[0:12]
    
if __name__ == "__main__":
    print(compute(10**16))
    print("--- %s seconds ---" % (time.time() - start_time))
    