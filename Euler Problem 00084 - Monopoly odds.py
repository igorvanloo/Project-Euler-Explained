#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:40:53 2021

@author: igorvanloo
"""

'''
Project Euler Problem 80

Monopoly problem 

Im going to first define the cards, then for every roll (Using the random module) whatever it lands on I will add that
square to a list and either use the counter method from collections or simply count all 40 squares and return the 
highest ones

00 = GO
02 = Community chest 1
07 = Chance 1 
10 = JAIL
17 = Community chest 2
22 = Chance 2
30 = Go to Jail
33 = Community chest 3
36 = Chance 3


Anwser:
    101524
--- 0.030651092529296875 seconds ---
    
'''

import time, random
start_time = time.time()

def community_chest(count):
    #0 = nothing
    #1 = go to GO = 00
    #2 = Go to jail == 10
    count = count % 16
    options = [0,0,0,1,0,0,0,0,0,2,0,0,0,0,0,0]
    return options[count]

def chance(count):
    #0 = nothing
    #1 = Advance to GO = 00
    #2 = Go to JAIL = 10
    #3 = Go to C1 = 11
    #4 = Go to E3 = 24
    #5 = Go to H2 = 39
    #6 = Go to R1 = 5
    #7 = Go to next R (railway company) = 5,15,25,35
    #8 = Go to next R = 5,15,25,35
    #9 = Go to next U (utility company) = 12, 28
    #10 = Go back 3 squares. = -3
    count = count % 16
    options = [0,10,8,4,5,2,6,7,0,0,0,9,1,3,0,0]
    return options[count]

def dice_roll(x):
    roll_1 = random.randrange(1,x+1)
    roll_2 = random.randrange(1,x+1)
    if roll_1 == roll_2:
        roll_3 = random.randrange(1,x+1)
        roll_4 = random.randrange(1,x+1)
        if roll_3 == roll_4:
            roll_5 = random.randrange(1,x+1)
            roll_6 = random.randrange(1,x+1)
            if roll_5 == roll_6:
                return 0
            else:
                return roll_1 + roll_2 + roll_3 + roll_4 + roll_5 + roll_6
        else:
            return roll_1 + roll_2 + roll_3 + roll_4
    else:    
        return roll_1 + roll_2

def compute():
    number_of_rolls = 0
    squares_landed_on = []
    current_square = 0
    community_chest_count = 0
    chance_count = 0
    
    while True:
        dice = dice_roll(4)
        if dice == 0:
            current_square = 10
            squares_landed_on.append(current_square)

        else:
            current_square += dice
            current_square %= 39
            
            if current_square == 2 or current_square == 17 or current_square == 33:
                
                card = community_chest(community_chest_count)
                if card == 1:
                    current_square = 0
                elif card == 2:
                    current_square = 10
                community_chest_count += 1
                    
            elif current_square == 7 or current_square == 22 or current_square == 36:
                
                card = chance(chance_count)
                if card == 1:
                    current_square = 0
                elif card == 2:
                    current_square = 10
                elif card == 3:
                    current_square = 11
                elif card == 4:
                    current_square = 24
                elif card == 5:
                    current_square = 39
                elif card == 6:
                    current_square = 5
                elif card == 7:
                    if current_square < 5 or current_square >= 35:
                        current_square = 5
                    elif current_square >= 5 and current_square < 15:
                        current_square = 15
                    elif current_square >= 15 and current_square < 25:
                        current_square = 25
                    elif current_square >= 25 and current_square < 35:
                        current_square = 35
                        
                elif card == 8:
                    if current_square < 5 or current_square >= 35:
                        current_square = 5
                    elif current_square >= 5 and current_square < 15:
                        current_square = 15
                    elif current_square >= 15 and current_square < 25:
                        current_square = 25
                    elif current_square >= 25 and current_square < 35:
                        current_square = 35
                elif card == 9:
                    if current_square < 12 or current_square >= 28:
                        current_square = 12
                    else:
                        current_square = 28
                elif card == 10:
                    current_square -= 3
                    
                chance_count += 1
                
            elif current_square == 30:
                current_square = 10
                
            squares_landed_on.append(current_square)
            
        number_of_rolls += 1
        if number_of_rolls == 50000:
            break
    
    squares_count = []
    for x in range(0, 40):
        squares_count.append([squares_landed_on.count(x), x])
    
    squares_count = sorted(squares_count)
    return str(squares_count[-1][1]) + str(squares_count[-2][1]) + str(squares_count[-3][1])
        

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))