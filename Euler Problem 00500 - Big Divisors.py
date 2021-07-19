#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 01:04:18 2021

@author: igorvanloo
"""
'''
Project Euler Problem 500

The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2^500500 divisors.
Give your answer modulo 500500507.

Reasoing

if n = p1^a * p2^b * p3^c * ...
then d(n) = (a+1)(b+1)(c+1)...

Found that d(p#n) = 2^n where p#n = product of all primes till n
so d(2 * 3 * 5 * ... * 7376507) = (1+1)(1+1)...(1+1) = 2^500500, => 2 * 3 * 5 * ... * 7376507 is an upper bound for n

we we are trying to find d(n) = 2^500500 = (a+1)(b+1)(c+1)... such that n = p1^a * p2^b * p3^c * ... is minimized

d(2) = 2^1
d(4) = 2^1 * 3^1
d(8) = 2^3 * 3^1 because 2^1 * 3^1 * 5^1 > 2^3 * 3^1 because 5 > 4
d(16) = 2^3 * 3^1 * 5^1 because 16 > 9 > 5
d(32) = choice between 25 > 16 > 9 > 7 so 2^3 * 3^1 * 5^1 * 7^1
d(64) = choice between 49 > 25 > 16 > 9 so 2^3 * 3^3 * 5^1 * 7^1

We can see that we can build them from the previous d(n)

So our algorithm must choose to increase one of the powers to the next power of 2 or add a new primes

Anwser:
    35407281
--- 2.399091958999634 seconds ---
'''

import time, math, eulerlib
start_time = time.time()


def compute2(): #Works faster but still too slow
    possibleprimes = eulerlib.primes(10000000)
    print("Primes Ready")
    
    options = [[x,1] for x in possibleprimes]
    print("Options Ready")
    
    total = 1
    
    for z in range(10000):
        if z % 10000 == 0:
            print(z)
        minimum, position = options[0][0], 0
        for pos in range(len(options)):
            
            if options[pos][0] < minimum:
                minimum, position = options[pos][0], pos
            elif options[pos][1] == 1 and options[pos+1][1] == 1:
                break
        a, b = options[position] 
        options[position] = [minimum**2, 2]
        total *= a
        total %= 500500507 

        
    return total

def compute1(): #Works but is too slow
    possibleprimes = eulerlib.primes(10000000)
    print("Primes Ready")
    
    terms = []
    
    for z in range(200):
        if z % 100 == 0:
            print(z)
        value = possibleprimes[0]
        terms.append(value)
        possibleprimes[0] = (possibleprimes[0])**2
        possibleprimes = sorted(possibleprimes)

    print("Calculating Total")
    total = 1
    for y in terms:
        total *= y
        total %= 500500507
        
    return total

def compute(): #Finally works
    possibleprimes = eulerlib.primes(7376507)
    print("Primes Ready")
    
    options = possibleprimes
    options += [x**2 for x in eulerlib.primes(2716)]
    options += [x**4 for x in eulerlib.primes(53)]
    options += [x**8 for x in eulerlib.primes(8)]
    options += [x**16 for x in [2,3]]
    options += [2**32]
    print("All Options Ready")

    possibleprimes = sorted(options)[::-1]
    print("Sorted Ready")

    total = 1
    
    for z in range(500500):
        total *= possibleprimes.pop(-1)
        total %= 500500507
        
    return total
        
        
if __name__ == "__main__":
    print(compute())
    #print(compute1())
    #print(compute2())
    print("--- %s seconds ---" % (time.time() - start_time))