#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:13:08 2020

@author: igorvanloo
"""

'''
Project Euler Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible 
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first 
example having seven primes among the ten generated numbers, yielding the family: 
    56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
    Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
with the same digit, is part of an eight prime value family.

because of modulo we know there needs to be 3 digits changed 

Anwser:
    121313
--- 0.754676103591919 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True
    
def family_creator(x):
    duplicates = []
    final_family = []
    temp_str = str(x)
    a = list(set(str(x))) #testing value
    b = [str(x) for x in range(0,10)] # replacement value
    
    for i in range(len(a)):
        count = 0
        for j in range(len(temp_str)):
            if temp_str[j] == a[i]:
                count += 1
        if count >= 2:
            duplicates.append([a[i], count])
                
    for i in range(len(duplicates)):
        family =[]
        for j in range(len(b)):
            family.append(temp_str.replace(duplicates[i][0], b[j], duplicates[i][1]))
        final_family.append(family)
    
    return final_family
            
def compute():
    primes = eulerlib.primes(1000000)
    good_primes = [x for x in primes if len(str(x))-len(set(str(x))) >= 3]
    
    for x in range(len(good_primes)):

        temp_family = family_creator(good_primes[x])
        
        for y in range(len(temp_family)):
            count = 0
            for z in range(10):
                if is_prime(int(temp_family[y][z])) == True:
                    count += 1
                    if count == 8:
                        return temp_family[y]
            
def compute1():
    primes = eulerlib.primes(1000000)
    goodprimes = []
    for p in primes:
        for c in range(0,10):
            if str(p).count(str(c)) == 3:
                goodprimes.append([p,c])
                
    for p in goodprimes:
        count = 0
        for c in range(1,10):
            if is_prime(int(str(p[0]).replace(str(p[1]),str(c),3))):
                count += 1
        if count == 8:
            return p[0]
            break
        
if __name__ == "__main__":
    #print(compute())
    print(compute1())
    print("--- %s seconds ---" % (time.time() - start_time))