# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 12:31:19 2022

@author: igorvanloo
"""
'''
Project Euler Problem 709

Every day for the past n days Even Stevens brings home his groceries in a plastic bag. 
He stores these plastic bags in a cupboard. 
He either puts the plastic bag into the cupboard with the rest, or else he takes an even number of the existing bags 
(which may either be empty or previously filled with other bags themselves) and places these into the current bag.

After 4 days there are 5 possible packings and if the bags are numbered 1 (oldest), 2, 3, 4, they are:

Four empty bags,
1 and 2 inside 3, 4 empty,
1 and 3 inside 4, 2 empty,
1 and 2 inside 4, 3 empty,
2 and 3 inside 4, 1 empty.

f(0) = 1
f(1) = 1: 1 empty bag
f(2) = 1: 2 empty bags
f(3) = 2: 3 empty bags, 1 and 2 inside 3
f(4) = 5: Example

OEIS search: https://oeis.org/A000111 the 8th value is 1385

https://mathworld.wolfram.com/EulerZigzagNumber.html
https://mathworld.wolfram.com/EntringerNumber.html

Anwser:
    773479144
--- 127.68839716911316 seconds ---
'''
import time
start_time = time.time()

def E(n, k):
    #https://mathworld.wolfram.com/EntringerNumber.html
    #E(n, n) = f(n)
    array = [[0]*(k + 1) for k in range(n + 1)]
    array[0][0] = 1
    mod = 1020202009
    for i in range(1, n + 1):
        if i % 1000 == 0:
            print(i)
        for j in range(1, i + 1):
            array[i][j] = ((array[i][j-1] + array[i - 1][i - j]) % mod)
            #print(i, j, array[i][j])
    return array[-1][-1] % mod

def f(n):
    return E(n, n)
    
if __name__ == "__main__":
    print(f(24680))
    print("--- %s seconds ---" % (time.time() - start_time))