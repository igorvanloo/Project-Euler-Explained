#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:29:40 2022

@author: igorvanloo
"""

'''
Project Euler Problem 

how many tiles around an x by x square

1 by 1 - 1*4 + 4 = 8
2 by 2 - 2*4 + 4 = 12
3 by 3 - 3*4 + 4 = 16
4 by 4 - 20
5 by 5 - 24
6 by 6 - 28
7 by 7 - 32
n by n - n*4 + 4 = 4*(n+1)

if we have 32 squares what can we form?
a 7 by 7 square 
a 1 by 1 + 5 by 5 square? no because there is  ring in the middle
a 2 by 2 and a 4 by 4 

so we can form multiple rings of square
1 by 1 could have a 3 by 3 and a 5 by 5 around it, etc
let n_i denote squares of width i
sum_{i = a to b = a + 1 + 2n} = 4*(a+1) + 4*(a+3) +... + 4*(a + 1 + 2n) = 4*(1 + 3 + 5 + ... + (1 + 2n)) = 4i(i + 2)
first few values, 12, 32, 60, 96

we could also have 4i(i + 1)
first few values are 8, 24, 48, 80

Anwser:
    1572729
--- 0.5276198387145996 seconds ---
'''
import time
start_time = time.time()
    
def compute(limit):
    pl = [] #possible laminae
    for x in range(1, int(limit/4)):
        temp1 = 4*(x + 1)
        if temp1 <= limit:
            pl.append(temp1)
    nl = [] #new laminae
    for i in range(len(pl) - 2):
        curr_sum = pl[i]
        curr = i + 2
        while curr_sum + pl[curr] <= limit:
            new_sum = curr_sum + pl[curr]
            nl.append(new_sum)
            curr_sum = new_sum
            if curr + 2 < len(pl):
                curr += 2
    return len(pl) + len(nl)

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))