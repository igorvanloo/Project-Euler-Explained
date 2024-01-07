# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 10:37:31 2023

@author: igorvanloo
"""
'''
Project Euler Problem 103

do near-optimum algorithm for n = 7

n = 1: {1}
n = 2: {1, 2}
n - 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}
n = 6: {11, 17, 20, 22, 23, 24}

correct n = 6: {11, 18, 19, 20, 22, 25}

n = 7: {20, 31, 38, 39, 40, 42, 45}

following the algorithm actually turns out to be the correct answer!

Anwser:
    20313839404245
--- 2.8998241424560547 seconds ---
'''
import time
from itertools import product
start_time = time.time()

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
        
def compute(near):
    current_best_set = near
    current_best_sum = sum(near)
    
    for A in product(*[list(range(x - 2, x + 3)) for x in near]):
        Asum = sum(A)
        
        if Asum < current_best_sum:
            if is_special_sum_set(A):
                print(A)
                current_best_set = A
                current_best_sum = Asum
    return "".join([str(x) for x in current_best_set])

if __name__ == "__main__":
    print(compute([20, 31, 38, 39, 40, 42, 45]))
    print("--- %s seconds ---" % (time.time() - start_time))
