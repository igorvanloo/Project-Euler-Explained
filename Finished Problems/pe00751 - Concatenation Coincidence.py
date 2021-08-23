#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:00:17 2021

@author: igorvanloo
"""

'''
Project Euler Problem 751

theta = 2.956938891377988

a1 = 2 => 2 < theta < 3
theta = 2.1, tau = 2.222...
theta = 2.2, tau = 2.2234...
theta = 2.3, tau = 2.23...

So we pick theta = 2.2
Repeat

Anwser:
    2.223561019313554106173177
--- 0.0018596649169921875 seconds ---
'''

import time, math

def sequence(theta, length):
    b1 = theta
    tau = str(math.floor(b1)) + "."
    
    while len(tau) < (length):
        floorb1 = math.floor(b1)
        bn = floorb1 * (b1 - floorb1 + 1)
        tau += str(math.floor(bn))
        b1 = bn
    return (tau[:length])

def compute(length):
    curr = "2."
    while len(curr) <= length:
        for x in range(0, 10):
            temp_curr = curr + str(x)
            if (temp_curr) == sequence(float(temp_curr), len(temp_curr)):
                curr += str(x)                
    return (curr)[:length]

if __name__ == "__main__":
    start_time = time.time()
    print(compute(26))
    print("--- %s seconds ---" % (time.time() - start_time))