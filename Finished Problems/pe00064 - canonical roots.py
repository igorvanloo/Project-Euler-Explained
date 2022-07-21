#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:34:51 2020

@author: igorvanloo
"""

'''
Project Euler Problem 64

we find the floor of the sqrt(n) this is our a0 then the equation becomes a0 + 1/(1/(sqrt(n) - a0)
then a1 = floor(sqrt(n) - a0) and so on we stop once we get that sqrt(n) - ak =                                                                            

Anwser:
    1322
--- 0.24978423118591309 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()


def is_quadratic(x):
    cube__root = (x**(1/2))
    if round(cube__root) ** 2 == x:
        return True
    return False

def canonical_form(x):
    if is_quadratic(x) == True: #Start by making sure its not a perfect square
        return []
    else:
        m0 = 0
        d0 = 1
        a0 = math.floor(math.sqrt(x)) #These are the starting values
        #test_mn = d0*a0 - m0
        #test_dn = (x - test_mn**2)/d0
        #test_an = math.floor((math.sqrt(x) + test_mn) / test_dn) #These are the tesr values, if we encounter them twice its over
        #print(test_mn, test_dn, test_an)
        #count = 0
        temp_list = []
        while True:
            mn = int(d0*a0 - m0) 
            dn = int((x - mn**2)/d0)
            an = int(math.floor((math.sqrt(x) + mn) / dn)) #new values
            temp_list.append(an)
            if an == 2*math.floor(math.sqrt(x)):
                break
            
            m0 = mn
            d0 = dn
            a0 = an #Replace values
    return temp_list

def compute(limit):
    count = 0
    for x in range(1,limit + 1):
        if len(canonical_form(x)) % 2 != 0:
            count += 1
    return count

if __name__ == "__main__":
    print(compute(9990))
    print("--- %s seconds ---" % (time.time() - start_time))