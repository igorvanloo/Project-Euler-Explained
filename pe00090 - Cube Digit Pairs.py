#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:20:18 2021

@author: igorvanloo
"""

'''
Project Euler Problem 90

Only (10 C 6)^2 = 44100 combinations to check, just brute force
Anwser:
    1217
--- 0.3234109878540039 seconds ---
'''

import time

def dicecomb(): #Produces all dice combinations, there are 10 C 6 = 210
    dicecombs = set()
    for a in range(0,10):
        for b in range(0,9):
            for c in range(0,8):
                for d in range(0,7):
                    for e in range(0,6):
                        for f in range(0,5):
                            if len(set([a,b,c,d,e,f])) == 6:
                                dicecombs.add(tuple(sorted((a,b,c,d,e,f))))
    return list(dicecombs)

def valid_dice_pair(dice1, dice2):
    #Dice 1 and Dice 2 are both tuples
    square_numbers = [(0,1), (0,4), (0,9), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1)]
    squares_generated = set()
    for x in dice1:
        for y in dice2:
            if x == 6 or x == 9:
                squares_generated.add((6,y))
                squares_generated.add((9,y))
                squares_generated.add((y,9))
                squares_generated.add((y,6))
            elif y == 6 or y == 9:
                squares_generated.add((6,x))
                squares_generated.add((9,x))
                squares_generated.add((x,9))
                squares_generated.add((x,6))     
            else:
                squares_generated.add((x,y))
                squares_generated.add((y,x))
    for x in square_numbers:
        if x not in squares_generated:
            return False 
    return True

def compute():
    dice = dicecomb()
    count = 0
    for x in range(len(dice)):
        for y in range(x+1,len(dice)):
            if valid_dice_pair(dice[x], dice[y]):
                count += 1
    return count

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))