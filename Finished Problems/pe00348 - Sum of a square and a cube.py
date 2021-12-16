#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:54:23 2021

@author: igorvanloo
"""

'''
Project Euler Problem 348

Tried to do something smart, but in the end brute force is the way by picking a random upper bound
Tried 10^8 first then 10^9 and it was enough, not a very smart way

Anwser:
    1004195061
--- 19.71703600883484 seconds ---
'''

import time, math
start_time = time.time()

def generate_palindromes(digits):
    if digits == 1:
        return [1,2,3,4,5,6,7,8,9]
    else:
        palindrome = []
        if digits % 2 == 0:
            t = 10**(digits//2)
            for x in range(int(t/10), t):
                palin = t*x + int(str(x)[::-1])
                palindrome.append(palin)
        else:
            t = 10**(digits//2)
            for c in range(9,0,-1):
                for x in range(int(t/10), t):
                    palin = int(str(x) + str(c) + (str(x)[::-1]))
                    palindrome.append(palin)
    return palindrome

def compute():
    total = 0
    array = dict()
    for cb in range(2, int(10**(9/3)) + 1):
        #print(cb)
        for sq in range(2, int(10**(4.5)) + 1):
            t = cb*cb*cb + sq*sq
            if str(t) == str(t)[::-1]:
                if t in array:
                    array[t] += 1
                else:
                    array[t] = 1
    for x in array.keys():
        if array[x] == 4:
            print(x)
            total += x
    return total

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))