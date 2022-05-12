#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:30:59 2022

@author: igorvanloo
"""

'''
Project Euler Problem 185

90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct

Lets assume our number starts with 0
0342 : 2 correct
0794 : 0 correct
9458 : 2 correct
4109 : 1 correct
1545 : 2 correct
2531 : 1 correct 

Then number starts with 00 
but 0794 : 0 correct, therefore it cannot start with 00

Anwser:

'''
import time, math
start_time = time.time()

def rec(guess, pos, mask, values, goal):
    print(mask)
    possib = []
    #print(guess, pos, mask, values)
    
    
    new_values = {}
    for v in values:
        #print(guess, v[pos])
        if str(guess) == v[pos]:
            new_values[v] = (values[v] - 1)
        else:
            new_values[v] = (values[v])
            
        if new_values[v] < 0:
            return []
        
    if pos == goal - 1:
        correct_guess = True
        for v in new_values:
            if new_values[v] != 0:
                correct_guess = False
        
        if correct_guess:
            print(mask)
            return [mask]
        else:
            return []
    
    for x in range(0, 10):
        possib += rec(x, pos + 1, mask + str(x), new_values, goal)
    
    return possib
    
def compute():
    values = {
        str(90342):2,
        str(70794):0,
        str(39458):2,
        str(34109):1,
        str(51545):2,
        str(12531):1}
    
    values2 = {
        str(5616185650518293):2,
        str(3847439647293047):1,
        str(5855462940810587):3,  
        str(9742855507068353):3,  
        str(4296849643607543):3,  
        str(3174248439465858):1,  
        str(4513559094146117):2,  
        str(7890971548908067):3,  
        str(8157356344118483):1,  
        str(2615250744386899):2,  
        str(8690095851526254):3,  
        str(6375711915077050):1,  
        str(6913859173121360):1,  
        str(6442889055042768):2,  
        str(2321386104303845):0,  
        str(2326509471271448):2,  
        str(5251583379644322):2,  
        str(1748270476758276):3,  
        str(4895722652190306):1,  
        str(3041631117224635):3,  
        str(1841236454324589):3,  
        str(2659862637316867):2}
    
    for x in range(0, 10):
        print(x)
        t = rec(x, 0, str(x), values2, len(str(5616185650518293)))
        if t != []:
            return t[0]
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))