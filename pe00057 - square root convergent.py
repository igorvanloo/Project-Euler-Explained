#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:07:19 2020

@author: igorvanloo
"""

'''
Project Euler Problem 57

let a(n) denote the nth iteration 
a(1) = 1 + 1/2 = 3/2
notice a(2) = 1 + 1/(1 + a(1)) = 1 + 1/(5/2) = 7/5

We get the recursion a(n+1) = 1 + 1/(1+a(n)) where a(1) = 3/2

let a(n) = num(n)/den(n) => num(n+1)/den(n+1) = 1 + 1/(1 + num(n)/den(n)) => num(n+1)/den(n+1) = 1 + 1/((den(n) + num(n))/den(n))
=> num(n+1)/den(n+1) = 1 + den(n)/(den(n) + num(n)) => num(n+1)/den(n+1) = ((den(n) + num(n)) + den(n))/(den(n) + num(n))
=> num(n+1)/den(n+1) = (2den(n) + num(n))/(den(n) + num(n))

Finally we get num(n+1) = 2den(n) + num(n) and den(n+1) = den(n) + num(n)

Anwser:
    153
--- 0.002134084701538086 seconds ---
'''

import time
start_time = time.time()

def compute(limit):
    count = 0
    numerator = 3
    denominator = 2
    for x in range(2,limit+1):
        temp_num = numerator + 2*denominator
        temp_denom = numerator + denominator
        
        if len(str(temp_num)) > len(str(temp_denom)):
            count += 1
    
        numerator = temp_num
        denominator = temp_denom
    return count

if __name__ == "__main__":
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))