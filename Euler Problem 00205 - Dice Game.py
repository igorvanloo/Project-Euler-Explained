#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:17:49 2021

@author: igorvanloo
"""

'''
Project Euler Problem 205

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form
0.abcdefg

Anwser:
    0.5731441
--- 0.054199934005737305 seconds ---    
'''

import time, math, random
start_time = time.time()

def colindice():
    mylist = [0]*37
    
    for x1 in [1,2,3,4,5,6]:
        for x2 in [1,2,3,4,5,6]:
            for x3 in [1,2,3,4,5,6]:
                for x4 in [1,2,3,4,5,6]:
                    for x5 in [1,2,3,4,5,6]:
                        for x6 in [1,2,3,4,5,6]:
                            temp = (x1+x2+x3+x4+x5+x6)
                            mylist[temp] += 1/(6**6)
    return (mylist)

def peterdice():
    mylist = [0]*37
    for x1 in [1,2,3,4]:
        for x2 in [1,2,3,4]:
            for x3 in [1,2,3,4]:
                for x4 in [1,2,3,4]:
                    for x5 in [1,2,3,4]:
                        for x6 in [1,2,3,4]:
                            for x7 in [1,2,3,4]:
                                for x8 in [1,2,3,4]:
                                    for x9 in [1,2,3,4]:
                                        temp = (x1+x2+x3+x4+x5+x6+x7+x8+x9)
                                        mylist[temp] += 1/(4**9)
    return (mylist)

def compute():
    pd = peterdice()
    cd = colindice()
    total = 0
    
    for y in range(9, 10):
        temptotal = 0
        for x in range(9, 37):
            if x > y:
                temptotal += pd[x]
        total += temptotal*cd[y]
    return round(total, 7)

def compute1(attempts):
    PP = [1,2,3,4]
    CC = [1,2,3,4,5,6]
    ppwins = 0
    for x in range(attempts):
        pptotal = 0
        for y in range(9):
            pptotal += random.choice(PP)
        
        cctotal = 0
        for y in range(6):
            cctotal += random.choice(CC)
            
        if pptotal > cctotal:
            ppwins += 1
            
    return ppwins/attempts

if __name__ == "__main__":
    #print(compute(100000))
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))