# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:58:23 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 182

Number of unconcealed messages is (gcd(e - 1, p - 1) + 1)(gcd(e - 1, q - 1) + 1) which I found at https://mysterytwister.org/media/challenges/pdf/mtc3-veselovsky-05-rsa-en.pdf

From there problem is simple

Answer:
    399788195976
--- 1.075488567352295 seconds ---
'''
import time, math
start_time = time.time()

def compute(p, q):
    phi = (p - 1)*(q - 1)
    values = {}
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            num = (math.gcd(e - 1, p - 1) + 1) * (math.gcd(e - 1, q - 1) + 1)
            if num in values:
                values[num] += e
            else:
                values[num] = e
    return values[min(values)]

if __name__ == "__main__":
    print(compute(1009, 3643))
    print("--- %s seconds ---" % (time.time() - start_time))
