# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:26:28 2023

@author: igorvanloo
"""
'''
Project Euler Problem 105

Copeied is_special_sum function from problem 103 and the problem is done

Anwser:
    73702
--- 1.364645004272461 seconds ---
'''
import time
start_time = time.time()

def ReadFile():  # Create the inital list
    file = open("C:/Users/IP176077/Dropbox/PC/Desktop/Python-Projects/Project-Euler-Related/0. Project Euler Files/0105_sets.txt")
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        x = x.rstrip()
        x = x.split(",")
        x = [int(y) for y in x]
        datalist.append(x)
    return datalist

def is_special_sum_set(A):
    
    l = len(A)
    
    #Generate all subsets
    subsets = [[] for x in range(l + 1)]
    sums = []
    for x in range(pow(2, l)):
        mask = bin(x)[2:]
        s = [A[i] for i, y in enumerate(reversed(mask)) if y == "1"]
        #print(mask, s)
        sum_s = sum(s)
        if sum_s in sums:
            #Test condition 1
            return False
        sums.append(sum_s)
        subsets[len(s)].append((s, sum_s))
    
    #Test condition 2
    max_sum = max([y for (_, y) in subsets[1]])
    
    for x in range(2, len(A) + 1):
        min_sum = min([y for (_, y) in subsets[x]])
        if min_sum < max_sum:
            return False
        max_sum = max([y for (_, y) in subsets[x]])
    
    return True        
        
def compute():
    sets = ReadFile()
    total = 0
    for i, A in enumerate(sets):
        if is_special_sum_set(A):
            total += sum(A)
    return total

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
