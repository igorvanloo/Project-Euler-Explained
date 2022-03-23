#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:14:30 2022

@author: igorvanloo
"""

'''
Project Euler Problem 216

Made a prime sieve based on this article: http://devalco.de/quadr_Sieb_2x%5E2-1.php

Anwser:
    5437849
--- 101.27085590362549 seconds ---
'''
import time
start_time = time.time()

def compute(limit):
    f = [int(2*n*n - 1) for n in range(limit + 1)]
    count = [1]*(limit + 1)
    for x in range(2, len(f)):
        div = f[x]
        if div > 1:
            for curr1 in range(x + div, limit + 1, div):
                while f[curr1] % div == 0:
                    f[curr1] //= div
                    count[curr1] = 0
            for curr2 in range(-x + div, limit + 1, div):
                while f[curr2] % div == 0:
                    f[curr2] //= div
                    count[curr2] = 0
    return sum(count[2:])

if __name__ == "__main__":
    print(compute(5*10**7))
    print("--- %s seconds ---" % (time.time() - start_time))