#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:48:56 2021

@author: igorvanloo
"""

'''
Project Euler Problem 121

Round 1 [R, B] = 1/2
Round 2 [R, B, R] = 1/3
Round 3 [R, B, R, R] = 1/4
Round 4 [R, B, R, R, R] = 1/5

Prob of winning is picking 3 or 4 blue

4 blue is simple 1/2 * 1/3 * 1/4 * 1/5 = 1/120 only one scenario
3 blue is trickier 
Scenario 1: Draw B from round 1, 2, 3 = 1/2 * 1/3 * 1/4 * 4/5
Scenario 2: Draw B from round 1, 2, 4 = 1/2 * 1/3 * 3/4 * 1/5
Scenario 3: Draw B from round 1, 3, 4 = 1/2 * 2/3 * 1/4 * 1/5
Scenario 4: Draw B from round 2, 3, 4 = 1/2 * 1/3 * 1/4 * 4/5

We can build a tree from this

        B                           R
                    [1 , 1]
                    
                   [1, 3, 2]        2 Blues = 1/2 * 1/3 = 1/6, 1 blue 1 red = 1/2 * 2/3 + 1/2 * 1/3 = 3/6, 2 red = 1/2 * 2/3 = 2/6
                 
                 [1, 6, 11, 6]       3 Blues = 1/6 * 1/4 = 1/24, 2 blue 1 red = 1/6 * 3/4 + 3/6 * 1/4 = 6/24
                                         2 red 1 blue = 2/6 * 1/4 + 3/6 * 3/4 = 11/24, 3 red = 2/6 * 3/4 = 6/24

We can build our new probabilities from our previous ones, this implies we should be using dynamic programming

Anwser:
    2308 = MonteCarlo simulation
--- 96.0902259349823 seconds ---

    2269
--- 0.00017189979553222656 seconds ---
'''

import time, math, random

def MonteCarlo(tries, turns):
    
    win = 0
    for x in range(tries):
        original = ["R", "B"]
        chosen = []
        
        for x in range(turns):
            choice = random.choice(original)
            #print(choice)
            chosen.append(choice)
            original.append("R")
            #print(original)
            
        if chosen.count("B") > chosen.count("R"):
            win += 1
    
    return math.floor(tries/win)

def compute(n):
    possib = []
    for x in range(2,n+2):
        possib.append([0]*x)
    
    possib[0][0], possib[0][1] = 1/2, 1/2
    for row in range(1, len(possib)):
        for y in range(len(possib[row])):
            
            if y == 0: #If we are on the first cell we can only come from the first cell of the row above (All Blue)
                possib[row][0] += (1/(row+2))*possib[row - 1][0]
                
            elif y == len(possib[row])-1: #If we are on the last cell we can only multiply by the prob of getting a red
                possib[row][y] += ((row+1)/(row+2))*possib[row - 1][y - 1]
                
            else: #We are in on the middle squares there are 2 scenarios
                
                #Case 1: multiply square diagonally left by number of reds in row
                #Case 2:multiply square diagonally right by number of blues in row
                possib[row][y] += ((row+1)/(row+2)) * possib[row - 1][y - 1] + (1/(row+2))*possib[row - 1][y]
                 
    return math.floor(1/sum(possib[-1][:((n+1)//2)]))

if __name__ == "__main__":
    start_time = time.time()
    print(compute(15))
    print("--- %s seconds ---" % (time.time() - start_time))