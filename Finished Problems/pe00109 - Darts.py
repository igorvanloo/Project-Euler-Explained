# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:46:27 2024

@author: igorvanloo
"""
'''
Project Euler Problem 109

Really simple problem

Just generate every possible checkout, there are 63 choices for first and second dart
63 = 20 + outer bull (singles) + 20 + inner bull (doubles) + 20(triples)
and 21 choices for last dart
total = 83349 combinations which is really small

Brute force check that if combination (x, y, z) is already accounted for do not add (y, x, z)

Anwser:
    38182
--- 0.42746567726135254 seconds ---
'''
import time
start_time = time.time()

def all_checkouts():
    S = [("S0", 0)] + [("S" + str(i), i) for i in range(1, 21)] + [("S25", 25)]
    D = [("D" + str(i), 2*i) for i in range(1, 21)] + [("D50", 50)]
    T = [("T" + str(i), 3*i) for i in range(1, 21)]
    
    checkout = [[] for _ in range(171)]
    for (x1, v1) in S + D + T:
        for (x2, v2) in S + D + T:
            for (x3, v3) in D:
                s = v1 + v2 + v3
                if (x2, x1, x3) not in checkout[s]:
                    checkout[s].append((x1, x2, x3))
    return checkout
    
def compute(score):
    checkouts = all_checkouts()
    return sum(len(checkouts[i]) for i in range(score))

if __name__ == "__main__":
    print(compute(100))
    print("--- %s seconds ---" % (time.time() - start_time))
