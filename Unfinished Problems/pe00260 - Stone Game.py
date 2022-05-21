#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:18:58 2022

@author: igorvanloo
"""
'''
Project Euler Problem 260

I've been working on this problem for so long please end my suffering
But actually it's quite fun! If you're reading this hello, sadly my code has a long way to go here

    173895 - Limit is 100
--- 84.71858811378479 seconds ---

    1358608 - Limit is 200
--- 1421.447793006897 seconds ---

Anwser:

'''
import time
from functools import cache
start_time = time.time()

def srt(atuple):
    return tuple(sorted(atuple))

@cache
def move_checker(atuple, player):
    x, y, z = atuple
    
    candidate = set()
    for a in range(1, x + 1):
        candidate.add((x - a, y, z))
        candidate.add((x - a, y - a, z))
        candidate.add(srt((x - a, y, z - a)))
        candidate.add((x - a, y - a, z - a))
        
    for b in range(1, y + 1):
         candidate.add(srt((x, y - b, z)))
         candidate.add(srt((x, y - b, z - b)))
         
    for c in range(1, z + 1):
           candidate.add(srt((x, y, z - c))) 
    
    #print(player, candidate)
    if (0, 0, 0) in candidate:
        if player == 1:
            return True #this position is winning for player 1
        else:
            return False #this position is losing for player 1 because player 2 will win
    else:
        if player == 1:
            if all([(move_checker(x, (player + 1) % 2) == False) for x in candidate]):
                #Every candidate move results in a position that is winning for player 2
                #So player 1 loses
                return False 
            else:
                return True
        else:
            if all([(move_checker(x, (player + 1) % 2) == True) for x in candidate]):
                #Every candidate move results in a position that is winning for player 1
                return True
            else:
                return False
                
def compute(limit):
    total = 0
    #iterations = ((limit + 1)*(limit*limit + 5 * limit + 6))//6      
    for x in range(limit + 1):
        print(x)
        for y in range(x, limit + 1):
            for z in range(y, limit + 1):
                if move_checker((x, y, z), 1) == False:
                    total += x + y + z        
    return total 

if __name__ == "__main__":
    print(compute(25))
    print("--- %s seconds ---" % (time.time() - start_time))
