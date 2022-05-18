#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:38:05 2022

@author: igorvanloo
"""
'''
Project Euler Problem 250

Similar to problem 249

I make an array such that array[x] = number of subsets such that sum of set = x % 250

we start with {} therefore array[0] = 1 (we need to remove this value later)

we start with x = 1
we go through all subsets we get the new subset {1} array[1] = 1

x = 4
we get {4}, {1,4} array[4] = 1, array[5] = 1

x = 27
we get {27}, {1, 27}, {4, 27}, {1, 4, 27} array[27] = 1, array[28] = 1, array[31] = 1, array[32] = 1

x = 256
we get {256}, {1, 256}, {4, 256}, {27, 256}, {1, 4, 256}, {1, 27, 256}, {4, 27, 256}, {1, 4, 27, 256}

If we have array[1] = a and x = 256 then, then array[7] += a

Although there is slight problem if we do this, our array updates as we get causing massive overflow, so we need to create
a duplicate array which stores the previous values

Anwser:
    1425480602091519
--- 13.320903778076172 seconds ---
'''
import time
start_time = time.time()

def compute(limit):
    mod = 10**16
    values = [pow(i, i, 250) for i in range(1, limit+1)]
    
    array = [1] + [0]*249
    array2 = [1] + [0]*249
    
    for x in values:
        
        for y in range(250):
            #print(x, y, array2[y])
            array[(x + y) % 250] += array2[y]
            array[(x + y) % 250] %= mod
        
        array2 = [x for x in array]    
        
    return (array[0] - 1) % mod

def compute2(limit): #Slightly cleaner code
    mod = 10**16
    values = [pow(i, i, 250) for i in range(1, limit+1)]
    array = [1] + [0]*249
    for x in values:
        array = [(array[y] + array[(x + y) % 250]) % mod for y in range(len(array))]
    return array[0] - 1

if __name__ == "__main__":
    print(compute2(250250))
    print("--- %s seconds ---" % (time.time() - start_time))
