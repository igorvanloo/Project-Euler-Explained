#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:01:24 2021

@author: igorvanloo
"""

'''
Project Euler Problem 493

70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.

What is the expected number of distinct colours in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).

Mathematical approach

Find the probability that one colour is not a part of the 20 balls
that is, the 20 balls are actually chosen from 60
so we have 60C20 / 70C20 to be that probability
therefore the probability that this colour was picked is 1 - 60C20 / 70C20
We do this for each colour 7(1 - 60C20 / 70C20)


Anwser:
    6.8186937 (Result after 10**7 iterations using monte carlo)
--- 223.13179397583008 seconds ---

6.818741802
--- 0.00011706352233886719 seconds ---
    
'''

import time, random, math

start_time = time.time()

def n_choose_r(n, r): #nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
    
def compute(x):
    
    distinctcolours = []
    
    for y in range(x):
        balls = ["R"]*10 + ["O"]*10 + ["Y"]*10 + ["G"]*10 + ["LB"]*10 + ["DB"]*10 + ["P"]*10

        templist = []
        for i in range(20):
            choice = random.choice(balls)
            templist.append(choice)
            balls.remove(choice)
        distinctcolours.append(len(set(templist)))
    
    total = 0 
    for z in range(1,8):
        total += distinctcolours.count(z) * z
    return total/x

if __name__ == "__main__":
    print(round(7*(1-(n_choose_r(60,20)/n_choose_r(70,20))), 9))
    print("--- %s seconds ---" % (time.time() - start_time))