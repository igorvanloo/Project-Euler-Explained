#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:40:43 2022

@author: igorvanloo
"""
'''
Project Euler Problem 286

Seems pretty simple, just srt up the game with memoization and use bisection algorithm to find correct q

Anwser:
    52.6494571953
--- 0.029756784439086914 seconds ---
'''
import time
from functools import cache
start_time = time.time()

@cache
def game(q, score, shots, needed_score):
    lose_chance = shots/q
    win_chance = 1 - lose_chance
    if score > needed_score:
        return 0
    if shots > 50:
        if score == needed_score:
            return 1
        else:
            return 0
    return win_chance*game(q, score + 1, shots + 1, needed_score) + lose_chance*game(q, score, shots + 1, needed_score)
        
def compute(needed_score):
    goal = 0.02
    accuracy = pow(10, -12)
    #Set up a standard bisection method to find q
    low = 50
    high = 1000
    while (high - low) > accuracy:
        mid = (high + low)/2
        if game(mid, 0, 1, needed_score) < goal:
            high = mid
        else:
            low = mid
    return round(high, 10)

if __name__ == "__main__":
    print(compute(20))
    print("--- %s seconds ---" % (time.time() - start_time))
