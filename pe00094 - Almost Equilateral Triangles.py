#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 01:48:03 2021

@author: igorvanloo
"""

'''
Project Euler Problem 94

       /|\
      / | \
  C  /  |  \ C
    /   |   \
   /    | B  \
  /     |     \
 /      |      \
/       |       \
- - - - - - - - -
    A       A

Consider the above triangle where C is the 2 sides and 2A = C +- 1

B is easily calculated by sqrt(C^2 - A^2)

We need the area of the triangle to be an integer, Area = 1/2 * 2AB = AB

We know 2A is always an integer => A is also an integer (because 2A is even)

Case 1
Let 2A = C - 1 => A = (C-1)/2 => Area = A*sqrt(C^2 - (C-1)^2 / 4) = A*sqrt((3C^2 + 2C - 1) / 4)
=> (3C^2 + 2C - 1) / 4 = k^2 => 3C^2 + 2C - 1 = 4k^2

Case 2
Let 2A = C + 1 => A = (C+1)/2 => Area = A*sqrt(C^2 - (C+1)^2 / 4) = A*sqrt((3C^2 - 2C - 1) / 4)
=> (3C^2 - 2C - 1) / 4 = k^2 => 3C^2 - 2C - 1 = 4k^2

Anwser:
    518408346
--- 0.00039196014404296875 seconds ---
'''

import time, math, eulerlib

def is_quadratic(x):
    cube__root = (x**(1/2))
    if round(cube__root) ** 2 == x:
        return True
    return False

def compute1(): #Go through C check if it quadratic I think reverese way will be faster
    
    total = 0
    C = 5
    while True:
        if 3*C + 1 > 10**9:
            break
        else:
            if is_quadratic((3*C**2 - 2*C - 1)/4):
                print(C)
                total += 3*C + 1
            
            elif is_quadratic((3*C**2 + 2*C - 1)/4):
                print(C)
                total += 3*C - 1 
            
            C += 1
    return total

def compute2(): #Actually it turned out to be pretty much the same speed ... so lets go one step further
    
    total = 0
    k = 1
    while True:
        if k > math.sqrt(((10**9)/2 - 1)**2 - 1):
            break
        
        C1 = (2*(math.sqrt(3*k*k + 1)) + 1)/3 #Roots of 3C^2 - 2C - 1 - 4k^2 = 0, 2A = C + 1
        if float(C1) == int(C1): #Test if C is an integer, if it is we have found a solution
            total += 3*C1 + 1
            print(3*C1 + 1)
            
        C = (2*(math.sqrt(3*k*k + 1)) - 1)/3 #Roots of 3C^2 + 2C - 1 - 4k^2 = 0, 2A = C - 1
        if float(C) == int(C): #Test if C is an integer, if it is we have found a solution
            total += 3*C - 1
            print(3*C - 1)
        k += 1
            
    return total

def compute(limit):
    total = 0
    n = 1
    
    while True:
        
        C = (((7 - 4*math.sqrt(3))**n + (7 + 4*math.sqrt(3))**n + 1)/3) #Integer solutions of 3C^2 - 2C - 1 - 4k^2 = 0, 2A = C + 1
        
        C1 = (((2 + math.sqrt(3)) * (7 - 4*math.sqrt(3))**(n+1) - (math.sqrt(3) - 2)*(7 + 4*math.sqrt(3))**(n+1) - 1)/3) #Integer solutions of 3C^2 + 2C - 1 - 4k^2 = 0, 2A = C - 1)
        
        perC = 3*C + 1
        perC1 = 3*C1 - 1
        
        if perC > limit:
            break
            
        total += perC
        if perC1 > limit:
            break
            
        total += perC1
        n += 1
        
    return int(total)

if __name__ == "__main__":
    start_time = time.time()
    print(compute(10**9))
    print("--- %s seconds ---" % (time.time() - start_time))