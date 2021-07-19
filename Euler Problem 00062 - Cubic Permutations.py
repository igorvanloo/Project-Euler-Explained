#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 15:58:19 2020

@author: igorvanloo
"""

'''
Project Euler Problem 62

The cube, 41063625 (3453), can be permuted to produce two other cubes: 
    56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has 
    exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

Anwser:
    127035954683
--- 0.6492130756378174 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def permutations(number):
    final_list = []
    string = str(number)
    temp_permutations = list(itertools.permutations(string))
    for y in range(len(temp_permutations)):
            temp_var = "".join(str(temp_permutations[y][i]) for i in range(len(temp_permutations[y])))
            final_list.append(temp_var)
            
    return final_list
            
def is_cubic(x):
    cube__root = (x**(1/3))
    if round(cube__root) ** 3 == x:
        return True
    return False
        
def badcompute():
    
    num = [a for a in range(1,10000)]
    for y in range(len(num)):
        temp_list = sorted(list(set(permutations(num[y]**3))))
        temp_list = temp_list[::-1]
        valid_numbers = []
        for x in range(len(temp_list)):
            if int(temp_list[x]) < num[y]**3:
                break
            
            elif is_cubic(int(temp_list[x])) == True:
                valid_numbers.append(temp_list[x])
                
        if len(valid_numbers) == 5:
            return num[y]
            
        elif len(valid_numbers) == 3:
            print(num[y])

def compute():
    '''
    We take a look at the sorted list that each num^3 gives, we note that another number will produce the same list iff
    it is a permutation of num^3, therefore we create a list add it to a bigger list and if the occurence of any list
    is given 5 times we return the first instance of it occuring ^3 to result in the smallest one
    '''
    num = 0
    final_list = []
    
    while True:
        temp_list = sorted(str(num**3))
        final_list.append(temp_list)
        
        if final_list.count(temp_list) == 5:
            return (final_list.index(temp_list))**3
            break
        num += 1

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))