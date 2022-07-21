#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:25:24 2020

@author: igorvanloo
"""

'''
Project Euler Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 
918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an 
integer with (1,2, ... , n) where n > 1?

Anwser:
    932718654
--- 0.018409252166748047 seconds ---
'''

import time, math
start_time = time.time()

def compute():
    
    check = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    concatenated_product_list = []
    for z in range(2,10):
        for x in range(1,10**math.floor(9/z)):
            temp_str = ""
            for y in range(1,z+1):
                product = x*y
                temp_str += str(product)
                if sorted(temp_str) == check:
                    concatenated_product_list.append(int(temp_str))
    return max(concatenated_product_list), concatenated_product_list

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))