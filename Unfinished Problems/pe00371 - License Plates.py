#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 23:26:58 2021

@author: igorvanloo
"""

'''
Project Euler Problem 371

Lets try easier version:
    Every car has only 1 digit at the back, he wins if he sees 2 plates that sum up to 10
    
Whats the expected number of plates he needs to see?

Let Z denote the number of plates he needs to see

P{Z = 1} = 0 (Impossible he needs to see atleast 2)
P{Z = 2} = 9/10 * 1/10 = 0.09

            1. If we see a 0 first, chance 1/10, now we need to get it in 2 tries so total is 1/10 * P{Z = 2}
P{Z = 3} =  2. If we see 5 first, 1/10, then if we get 0, 1/10 we need a 5 so 1/10. If we get not 0 or 5, 8/10 then we have 2 chances 2/10
            3. If we see anything else, x, 8/10, If we get a 0 or x, 2/10 then we only have one chance 1/10
               If we dont get 0, or x, 7/10 then we have 2 chances, 2/10. Total = 8/10 *(2/10*1/10 + 8/10*2/10)
         = 1/10*9/100 + 1/10*(1/100 + 16/100) + 8/10*(2/10*1/10 + 7/10*2/10) = 0.154
         = 

Made a monte carlo variation, which confirms these calculations

For the actual problem I get the estimate: 40.6629944 which is very close to the real answer

the problem is clearly dependent on the numbers 0 and 5

Anwser:

'''

import time, math, random
start_time = time.time()

def monte_carlo(goal, trials):
    
    E = {}
    for _ in range(trials):
        seen = set()
        Z = 1
        while True:
            v = random.randint(0, goal - 1)
            if goal - v in seen:
                break
            seen.add(v)
            Z += 1
        if Z in E:
            E[Z] += 1
        else:
            E[Z] = 1
    
    total = 0
    check_sum = 0
    for x in sorted(E):
        print(x, E[x]/trials)
        total += x*E[x]
        check_sum += E[x]/trials
        
    return total/trials, check_sum
        
if __name__ == "__main__":
    print(monte_carlo(1000, 10000000))
    print("--- %s seconds ---" % (time.time() - start_time))