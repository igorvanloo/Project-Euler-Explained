#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:34:42 2021

@author: igorvanloo
"""
'''
Project Euler Problem 153

z = a + bi
if z|d then z*|d

if z|d => d/(a+bi) = d(a-bi)/(a^2 + b^2) => (a^2 + b^2)|d

Now if a^2 + b^2 = d then d/z = z*
if a^2 + b^2 | d then d/z = d/(a^2+b^2) * z*

So for each d, we search for it's possible decompositions of 2 square numbers,
if we find a pair that divides we get 4 complex numbers which divide it 

Note for when you come back:
    
You got some base cases right but you're missing some edge cases like 3+3i divides 12

Anwser:

'''

import time, math
start_time = time.time()

def Divisors(x): #Find the divisors of a number
    divisors = set()
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.add(i)
            divisors.add(int(x/i))
    return sum(divisors)

def square_root_decomp(x):
    limit = int(math.floor(x**(1/2))) + 1
    decomp = []
    for z in range(1, limit):
        for y in range(1, limit):
            if z**2 + y**2 >= x + 1:
                break
            if x % (z**2 + y**2) == 0:
                decomp.append([z,y])
    return decomp

def compute(limit):
    array = [0] + [square_root_decomp(x) for x in range(1,limit + 1)]
    total = 0
    for x in range(1, len(array)):
        curr_sum = Divisors(x)
        for y in range(len(array[x])):
            a, b = array[x][y]
            temp = a**2 + b**2
            if temp == x:
                curr_sum += 2*a
            else:
                curr_sum += 2*a + 2*(int(x/temp))*a
        total += curr_sum
        #print(total)
        #print(x, curr_sum)
    return total
    
    

if __name__ == "__main__":
    print(compute(49))
    print("--- %s seconds ---" % (time.time() - start_time))