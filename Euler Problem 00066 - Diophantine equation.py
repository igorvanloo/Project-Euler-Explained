#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:37:49 2020

@author: igorvanloo
"""

'''
Project Euler Problem 66

Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

Anwser:
    [16421658242965910275055840472270471049, 661]
--- 0.02387404441833496 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def canonical_form1(x):
    if is_quadratic(x) == True: #Start by making sure its not a perfect square
        return []
    else:
        m0 = 0
        d0 = 1
        a0 = math.floor(math.sqrt(x)) #These are the starting values
        test_mn = d0*a0 - m0
        test_dn = (x - test_mn**2)/d0
        test_an = math.floor((math.sqrt(x) + test_mn) / test_dn) #These are the test values, if we encounter them twice its over
        count = 0
        temp_list = [a0]
        while count != 2:
            mn = int(d0*a0 - m0) 
            dn = int((x - mn**2)/d0)
            an = int(math.floor((math.sqrt(x) + mn) / dn)) #new values
            if mn == test_mn and dn == test_dn and an == test_an:
                count += 1 
            temp_list.append(an)
            m0 = mn
            d0 = dn
            a0 = an #Replace values
    
    return temp_list[:-2]

def continued_fraction(x):

    m0 = 0
    d0 = 1
    a0 = math.floor(math.sqrt(x)) #These are the starting values
    temp_list = [a0]
    while True:
        mn = int(d0*a0 - m0) 
        dn = int((x - mn**2)/d0)
        an = int(math.floor((math.sqrt(x) + mn) / dn)) #new values
        temp_list.append(an)
        #if an == 2*math.floor(math.sqrt(x)):
            #break
        if len(temp_list) == 100:
            break
        m0 = mn
        d0 = dn
        a0 = an #Replace values
    return temp_list

def overall_fraction(cf):
    numerator = 1
    denominator = cf[0]
    
    for x in range(1,len(cf)):
        denominator, numerator =cf[x]*denominator + numerator, denominator
                
    return denominator, numerator

def is_quadratic(x):
    cube__root = (x**(1/2))
    if round(cube__root) ** 2 == x:
        return True
    return False

def convergent(D):
    cf = continued_fraction(D)
    h0, h1 = 1, cf[0]
    k0, k1 = 0, 1
    if h1**2 - D*k1**2 == 1:
        return [h1, D]
    else:
        x = 1
        while True:
            hn = cf[x]*h1 + h0
            kn = cf[x]*k1 + k0
            if hn**2 - D*kn**2 == 1:
                break
            h0 = h1
            h1 = hn
            k0 = k1
            k1 = kn
            x += 1
    return [hn, D]

def compute1(limt):
    final_list = []
    for D in range(2,limt + 1):
        if is_quadratic(D) == False: #Start by making sure its not a perfect square
            final_list.append(convergent(D))
    return max(final_list)
            
            
def compute():
    final_list = []
    for D in range(2,1001):
        if is_quadratic(D) == True: #Start by making sure its not a perfect square
            pass
        else:
            temp_list = canonical_form1(D)
            temp_list = temp_list[::-1]
            
            if len(temp_list) % 2 != 0:
                denom, numer = overall_fraction(temp_list)
                denom, numer = 2*denom**2 + 1, 2*denom*numer
            else:
                denom, numer = overall_fraction(temp_list)

            final_list.append([denom, D])
    return max(final_list)


        
if __name__ == "__main__":
    print(compute1(500))
    print("--- %s seconds ---" % (time.time() - start_time))