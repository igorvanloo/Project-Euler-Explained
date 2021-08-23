#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:09:10 2021

@author: igorvanloo
"""
'''
Project Euler Problem 99

Largest exponential 

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm 
that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over 
three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
 base/exponent pair on each line, determine which line number has the greatest numerical value.

Anwser:
    (895447, 504922)
    709
--- 0.0018527507781982422 seconds ---   
'''

import time, math
start_time = time.time()

def ReadFile(): #Create the inital list 
    file = open("/Users/igorvanloo/Dropbox/My Mac (Igors-MacBook-Air.local)/Desktop/Project Euler/0. Files/p099_base_exp.txt")
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        pos = x.index(",")
        datalist.append([int(x[0:pos]),int(x[pos+1:])])
    return datalist

exponents = ReadFile()

def compute():
    maximum = 525805*math.log(519432, 519432)
    base = 0
    exp = 0
    
    for x in range(1,len(exponents)):
        if exponents[x][1]*math.log(exponents[x][0], 519432) > maximum:
            maximum = exponents[x][1]*math.log(exponents[x][0], 519432)
            base = exponents[x][0]
            exp = exponents[x][1]
    return exponents.index([base, exp]) + 1

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
    