#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:01:49 2020

@author: igorvanloo
"""

'''
Project Euler Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can 
work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes

Anwser:
    748317
    Very slow
'''

import time, math, eulerlib
start_time = time.time()


def truncate_primes(x):
    list2 = []
    str1 = str(x)
    a = 1
    for i in range(1, len(str1) + 1):
        list2.append(int(str1[0:i]))
        list2.append(int(str1[-i:]))
    return set(list2)

def compute():
    final_list = []
    count = 0
    primes = eulerlib.primes(10000000)
    for x in range(5, len(primes)):
        
        
        if (primes[x]%10) % 2 == 0 or (primes[x]%10) % 5 == 0 :
            pass
        if x % 1000 == 0:
            print(x)
        else:
            temp_list = truncate_primes(primes[x])
            if set(temp_list) == set(temp_list).intersection(set(primes)):
                count += 1
                final_list.append(primes[x])
                print(count, primes[x])
                
                if count == 11:
                    return sum(final_list), final_list

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))