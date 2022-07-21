#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:32:05 2020

@author: igorvanloo
"""

'''
Project Euler Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

It ends in a 0 therefore if a^2 = 1_2_3_4_5_6_7_8_9_0, a must end in a 0, 
the maximum it can be is 1929394959697989990 the sqrt is 1389026623.1062636
the minimum is 1020304050607080900 the sqrt is 1010101010.1010101 so we search from 1010101010 till 1389026620

solution 2:
    it ends in 0 therefore 1_2_3_4_5_6_7_8_900 it will look like this therefore we can search 1_2_3_4_5_6_7_8_9
    then multiply by 10. Minimum is 101010101

Anwser:
    1389019170
--- 0.0016338825225830078 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    for x in range(1389026620, 1010101010, -10):
        number = str(x**2)
        temp_str = ""
        
        for y in range(0,len(number),2):
            temp_str += number[y]
            
        if temp_str == "1234567890":
            return x
    
def compute1():
    for x in range(1389026620, 101010100, -10):
        if str(x)[-2] == "7" or str(x)[-2] == "3":
            if str(x**2)[::2] == "1234567890":
                return x

def compute2():
    start = 101010100
    end = 1389026620
    while start < end:
        if str((start+30)**2)[::2] == "1234567890":
            start += 30
            break
        if str((start+70)**2)[::2] == "1234567890":
            start += 70
            break
        start += 100
    return start
        
            

if __name__ == "__main__":
    print(compute2())
    print("--- %s seconds ---" % (time.time() - start_time))