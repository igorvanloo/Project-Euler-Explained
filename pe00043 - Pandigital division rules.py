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

Reasoning

d4 must be even [0,2,4,6,8]
(d3 + d4 + d5) % 3 == 0
d6 = 5
(d6 - d7 + d8) % 11 == 0 => 506, 517, 528, 539, 561, 572, 583, 594
d7d8d9 % 13 => 5286, 5390, 5728, 5832
d8d9d10 % 17 => 952867, 357289

Case 1 - _ _ _ _ 952867 remaining numbers = 0,1,3,4

d3 + d4 + d5 must be divisble by 3 and d5 = 9 => d3 + d4 must be divible by 3 => the choices are 0,3
but d4 must be even so d4 = 0 d3 = 3

Then we have 2 possibilities

1430952867
4130952867

Case 2 - _ _ _ _ 357289 remaining numbers = 0,1,4,6

d3 + d4 + d5 must be divisble by 3 and d5 =3 => d3 + d4 must be divible by 3 => the choices are 0,6

4 possibilities

1406357289
1460357289
4106357289
4160357289

Sum of all of these = 16695334890

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
    print(overall_list)       
    return sum(overall_list)                                             

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))