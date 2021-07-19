#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:17:04 2021

@author: igorvanloo
"""

'''
Project Euler Problem 719

Anwser:
128088830547982
--- 2972.8279888629913 seconds ---
'''

import time, math
start_time = time.time()

def list_maker(anumber):
    length = len(str(anumber))
    array = []
    for x in range(length+1):
        array.append([])
    
    stack = [anumber]
    while len(stack) != 0:
        curr = stack.pop(0)
        array[len(str(curr))].append(curr)
        
        if len(str(curr)) == 1:
            continue
        
        remove_first_digit = int(str(curr)[1:])
        remove_last_digit = curr//10
        
        stack.append(remove_first_digit)
        stack.append(remove_last_digit)
    
    for x in range(length+1):
        array[x] = list(set(array[x]))
    return array 
        
def partition(number):
     answer = set()
     answer.add((number, ))
     for x in range(1, number):
         for y in partition(number - x):
             answer.add(tuple(((x, ) + y)))
        
     return sorted([x for x in answer])
    
def compute(limit):
    
    total = 0
    
    for z in range(1,limit+1):
        if z % 100000 == 0:
            print(z)
            print(total)
            print("--- %s seconds ---" % (time.time() - start_time))
        if z % 9 == 0 or z % 9 == 1:
            x = z**2
            temp_list = partition(len(str(x)))[:-1]
            
            for y in temp_list:
                temp_num = str(x)
                temp_total = 0
                value = ""
                
                for z in y:
                    value += temp_num[:z]
                    try:
                        temp_total += int(temp_num[:z])
                    except ValueError:
                        pass
                    temp_num = temp_num[z:]
                    #print(value)
                    
                if value == str(temp_total**2):
                    total += x
                    break
    return total
    
if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))