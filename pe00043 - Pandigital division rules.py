#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:20:53 2020

@author: igorvanloo
"""

'''
Project Euler Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in
 some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

Anwser:
    16695334890
--- 12.251658916473389 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    nine_digit_pandigital = list(itertools.permutations(range(0,10),10))
    overall_list = []
    for x in range(len(nine_digit_pandigital)):
        temp_var = "".join(str(nine_digit_pandigital[x][i]) for i in range(0, len(nine_digit_pandigital[x])))
        if int(temp_var[3]) % 2 == 0 and int(temp_var[2:5]) % 3 == 0 and int(temp_var[3:6]) % 5 == 0 \
            and int(temp_var[4:7]) % 7 == 0 and int(temp_var[5:8]) % 11 == 0 and int(temp_var[6:9]) % 13 == 0 \
                and int(temp_var[7:10]) % 17 == 0:
                    overall_list.append(int(temp_var))
                    
    return sum(overall_list)                                             

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))