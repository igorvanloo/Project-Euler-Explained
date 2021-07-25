#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:23:45 2020

@author: igorvanloo
"""

'''
Project Euler Problem 55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is 
Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, 
it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the 
computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first 
number to be shown to require over fifty iterations before producing a palindrome: 
    4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

N=5000 -> 12221 88
N=10000 -> 79497 215
N=50000 -> 79497 295
N=100000 -> 4964444694 583

Anwser:
    249
--- 0.047447919845581055 seconds ---
    
'''

import time
start_time = time.time()

def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

def compute(limit):
    not_lycherl_count = 0
    for x in range(1,limit+1):
        x = str(x)
        if is_palindrome(x):
            temp_var = str(int(x) + int(str(x[::-1])))
        else:
            temp_var = str(x)
            
        for y in range(50):
            temp_var = str(int(temp_var) + int(str(temp_var[::-1])))
            if is_palindrome(temp_var) == True:
                not_lycherl_count += 1
                break
    return limit - not_lycherl_count    
            
if __name__ == "__main__":
    print(compute(10000))
    print("--- %s seconds ---" % (time.time() - start_time))