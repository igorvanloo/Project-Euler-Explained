#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:56:21 2022

@author: igorvanloo
"""
'''
Project Euler Problem 389

https://en.wikipedia.org/wiki/Sicherman_dice

Tried to do it recursively, didn't work

I have done something on sicherman dice before so I think generating functions would work
Anwser:

'''
import time, math
from functools import cache
import random
start_time = time.time()

@cache
def paths(num_of_dice, depth):
    overall_total = 0
    n_o_d = num_of_dice
    div = (4*pow(6, 4))
    
    if depth == 0:
        #average = 2.5
        s = 4
        
    elif depth == 1:
        #average = 3.5
        s = 6
        
    elif depth == 2:
        #average = 4.5
        s = 8
        
        min_sum = 1*n_o_d #Minimum sum = 1*n_o_d
        max_sum = s*n_o_d #Maximum sum = sides*n_o_d
        print("Dice currently has " + str(s) + " sides range is " + str(min_sum) + " to " + str(max_sum), n_o_d)
        total = 0
        #We have reached final stage, go through each possible sum
        for x in range(min_sum, max_sum + 1):
            total += x
        total /= (max_sum + 1 - min_sum)
        
        return total
        
    '''elif depth == 3:
        s = 12
        
    elif depth == 4:
        s = 20
        '''
        
    min_sum = 1*n_o_d #Minimum sum = 1*n_o_d
    max_sum = s*n_o_d #Maximum sum = sides*n_o_d
    
    #First we throw 4-sided died - level 0
    #First we throw 6-sided died - level 1
    #First we throw 8-sided died - level 2
    #First we throw 12-sided died - level 3
    #First we throw 20-sided died - level 4
    #print("Dice currently has " + str(s) + " sides")
    for x in range(min_sum, max_sum + 1):
        #print("Evaluating x = " + str(x))
        temp = paths(x, depth + 1)
        #print("sum was " + str(temp))
        overall_total += temp
        print("overall total is " + str(overall_total))
        
    if depth == 0:
        return overall_total/div
    if depth == 1:
        return overall_total*pow(6, n_o_d)
    if depth == 2:
        return overall_total

if __name__ == "__main__":
    print(paths(1, 0))
    print("--- %s seconds ---" % (time.time() - start_time))
