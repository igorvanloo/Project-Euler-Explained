#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:03:26 2021

@author: igorvanloo
"""

'''
Project Euler Problem 141

n = d*q + r

By defintion r < d, lets assign d < q because we can simply swap d and q so r < d < q

Now r,d,q form a geometric sequence => let c be the geomteric factor

=> d = rc and q = rc^2, r, rc, rc^2, c must be rational and > 0 otherwise we could have a negative geometric sequence and non integer d,q

=> c = z/y = d/r = q/d

note that d/r * q/d = q/r = c^2 = z^2/y^2 => y^2 divides r because gcd(z,y) = 1, let x = r/y^2

=> r = xyy
   d = xyz
   q = xzz

we know that 0 < y < z => z >= 2

=> n = xyz * xzz + xyy = x^2yz^3 + xy^2

This means that 2 <= z < (10**12)**(1/3) = 10000

Anwser:
    878454337159
--- 9.328505039215088 seconds ---
'''
import time

def is_square(x):
    square_root = (x**(1/2))
    if round(square_root) ** 2 == x:
        return True
    return False

def compute(limit):
    #r = x * y * y, 
    #d = c * r = z * x * y,
    #q = c * d = z * z * x
    candidates = set()
    for z in range(2, int(limit**(1/3)) + 1):
        for y in range(1, z):
            if z*z*z*y + y*y > limit:
                break
            
            for x in range(1, int(limit/(y*z*z*z)) + 1):
                n = z*z*z*x*x*y + x*y*y
                if n > limit:
                    break
                else:
                    if is_square(n):
                        candidates.add(n)
                        
    return sum(candidates)

if __name__ == "__main__":
    start_time = time.time()
    print(compute(10**12))
    print("--- %s seconds ---" % (time.time() - start_time))