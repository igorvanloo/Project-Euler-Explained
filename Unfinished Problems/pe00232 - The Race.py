#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:46:33 2022

@author: igorvanloo
"""
'''
Project Euler Problem 232

Player one has an expected winning of 1/2

Player 2 always also has an expected winning of half, his probabilty of winning is (1/2)^T and his winnings is 2^(T-1)
Therefore he is expected to win 2^(T-1) * 2^(-T) = 1/2

Player 1 needs on average 200 turns to win 
If T = 8 he has a 1/256 chance to win 128 points, he needs 256 turns on average to win
If T = 7 he has a 1/128 chance to win 64 points, he needs 256 turns on average to win
If T = 6 he has a 1/64 chance to win 32 points, he needs 256 turns on average to win
If T = 5 he has a 1/32 chance to win 16 points, he needs 256 turns on average to win
If T = 4 he has a 1/128 chance to win 64 points, he needs 256 turns on average to win

Each round 4 things can happen
1) Player 1 wins Player 2 wins - Probability is 1/2 * (1/2)^T         = (1/2)^(T+1)
2) Player 1 wins Player 2 loses - Probability is 1/2 * (1 - (1/2)^T)  = 1/2 - (1/2)^(T+1)
3) Player 1 loses Player 2 wins - Probability is 1/2 * 1/2)^T         = (1/2)^(T+1)
4) Player 1 loses Player 2 loses - Probability is 1/2 * (1 - (1/2)^T) = 1/2 - (1/2)^(T+1)


Anwser:

'''

import time, math
from random import choice
start_time = time.time()

def monte_carlo(limit, T):
    trials = 0
    wins = 0
    while trials != limit:
        
        player_1_score = 0
        player_2_score = 0
        
        player_1_options = [0, 1]
        player_2_options = [x for x in range(2**T)]
        
        while True:
            if choice(player_1_options) == 0:
                player_1_score += 1
            
            if player_1_score == 100:
                break
            
            if choice(player_2_options) == 0:
                player_2_score += 2**(T-1)
            
            if player_2_score >= 100:
                wins += 1
                break
            
        trials += 1
        
    return wins, trials, wins/trials

if __name__ == "__main__":
    print(monte_carlo(100000))
    print("--- %s seconds ---" % (time.time() - start_time))