# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:46:50 2024

@author: igorvanloo
"""
'''
Project Euler Problem 122

Problem is to find optimal addition-chain exponentiation: https://en.wikipedia.org/wiki/Addition-chain_exponentiation

OEIS sequence: https://oeis.org/A003313

Tree like sequence makes sense. Build up tree using only elements that are on the path from node to root
use breadth first search

Anwser:
    1582
--- 69.39305782318115 seconds ---
'''
import time
start_time = time.time()

def compute(limit):
    
    v = [0]*(limit + 1)
    count = 1
    
    stack = [(1,)]
    currdepth = 1
    
    while count != limit:

        nextstack = []
        while stack != []:
            path = stack.pop()
            m = path[-1]
            
            for i in range(len(path) - 1, -1, -1):
                for j in range(i, -1, -1):
                    k = path[i] + path[j]
                    if k <= m:
                        break
                    if k <= limit:
                        if v[k] == 0:
                            v[k] = currdepth
                            count += 1
                            #print(k, count)
                            if count == limit:
                                stack = []
                                nextstack = []
                                break   
                        nextstack.append(path + (k,))
        stack = nextstack
        currdepth += 1
    
    return sum(v)

if __name__ == "__main__":
    print(compute(200))
    print("--- %s seconds ---" % (time.time() - start_time))
