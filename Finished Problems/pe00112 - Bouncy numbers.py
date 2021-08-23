#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 19:47:24 2021

@author: igorvanloo
"""

'''
Project Euler Problem 112

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; 
for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) 
are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers 
is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

Anwser:
    1587000
--- 1.8383889198303223 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()        
    
def is_bouncy(x):
    temp = list(str(x))
    test_increasing = sorted(temp)
    test_decreasing = sorted(temp)[::-1]
    
    if temp == test_increasing:
        return False
    if temp == test_decreasing:
        return False
    return True
    
def compute(x):
    bouncy_numbers = 0
    total = 1
    while bouncy_numbers/total != x:
        total += 1
        if is_bouncy(total) == True:
            bouncy_numbers += 1
    return total
        
if __name__ == "__main__":
    print(compute(0.99))
    print("--- %s seconds ---" % (time.time() - start_time))