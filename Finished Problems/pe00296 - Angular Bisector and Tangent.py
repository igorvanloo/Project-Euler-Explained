#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:01:11 2022

@author: igorvanloo
"""
'''
Project Euler Problem 296

Playing around with a geogebra tool https://www.geogebra.org/geometry/sbgbwtfe

We can observe a few interesting details
Triangle BCE and ACD are similar triangles. and DBE is an isoceles triangle and therefore BE = BD

Using the fact that k is an angular bisector of ACB we have that AD/BD = AC/BC => BD = AD * BC / AC
and AB = AD + BD, therefore we have that BD = (AB - BD) * BC / AC => BD * AC = AB * BC - BD * BC

=> BD * AC + BD * BC = BD * (AC + BC) = AB * BC => BE = BD = AB * BC / (AC + BC)

And this must be an integer, therefore we need all triangles such that

1. BC ≤ AC ≤ AB, BC + AC > AB
2. BC + AC + AB ≤ 100,000
3. AC + BC divides AB*BC

BruteForce works up to 10^3

Let d = gcd(AC, BC) => AC = d * AC', BC = d * BC' where gcd(AC', BC') = 1

we then have that BE = AB * BC' / (AC' + BC') clearly AC' + BC' cannot divide BC' therefore AC' + BC' | AB

Anwser:
    1137208419
--- 844.7029659748077 seconds ---
--- 91.18732213973999 seconds --- with pypy
'''
import time, math
start_time = time.time()

def BruteForce(limit):
    count = 0
    for BC in range(1, limit//3 + 1):
        for AC in range(BC, (limit - BC)//2 + 1):
            for AB in range(AC, min(BC + AC, limit - BC - AC + 1)):
                if BC + AC + AB <= limit:
                    if AB*BC % (AC + BC) == 0:
                        count += 1
                else:
                    break
    return count

def compute(limit):
    count = 0
    for BC in range(1, limit//3 + 1):
        for AC in range(BC, (limit - BC)//2 + 1):
            d = math.gcd(BC, AC)
            ACprime, BCprime = AC//d, BC//d
            cons = ACprime + BCprime
            ABmin = math.ceil(AC/cons)*cons
            ABmax = min(BC + AC, limit - BC - AC + 1)            
            for AB in range(ABmin, ABmax, cons):
                count += 1
    return count
    
if __name__ == "__main__":
    print(compute(10**5))
    print("--- %s seconds ---" % (time.time() - start_time))
