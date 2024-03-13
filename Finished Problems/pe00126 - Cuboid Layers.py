# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:15:43 2024

@author: igorvanloo
"""
'''
Project Euler Problem 126

We begin with an (a, b, c) cuboid clearly the number of cubes to cover it is

2ab + 2bc + 2ac

Few test cases using geogebra

          |   sum  | Layer 1 | Layer 2     | Layer 3     | Layer 4
(1, 1, 1) |    3   |    6    |  (+12)  18  |         56? |
(2, 1, 1) |    4   |    10   |  (+16)  26  |         60? |
(2, 2, 1) |    5   |    16   |  (+20)  36  |  (+28)  64  | 
(2, 2, 2) |    6   |    24   |  (+24)  48  |  (+32)  80  |   (+40) 120? 
(3, 2, 1) |    6   |    22   |  (+24)  46  |  (+32)  78  |   (+40) 118

Notice that the + in layer 2 is 4*sum and then increases by 8 each level

Hypothesis is 
num_of_cubs(a, b, c, l) = 2(ab + bc + ac) if l = 1
                        = num_of_cubs(a, b, c, l - 1) + 4*(a + b + c) + 8*(l - 2) if l > 2

if l = 2, num_of_cubs(a, b, c, 2) = 2(ab + bc + ac) + 4*(a + b + c)
if l = 3, num_of_cubs(a, b, c, 3) = (2(ab + bc + ac) + 4*(a + b + c)) + 4*(a + b + c) + 8
if l = 4, num_of_cubs(a, b, c, 4) = (2(ab + bc + ac) + 2*4*(a + b + c) + 8) + 4*(a + b + c) + 8*2
if l = 5, num_of_cubs(a, b, c, 5) = (2(ab + bc + ac) + 3*4*(a + b + c) + 8*3) + 4*(a + b + c) + 8*3
...
if l = n, num_of_cubs(a, b, c, n) = 2(ab + bc + ac) + (n - 1)*4*(a + b + c) + 8*(n - 1)(n - 2)/2
                                  = 2(ab + bc + ac) + 4(n - 1)(a + b + c + n - 2)

Now we just brute force

Answer:
    18522
--- 2.1923024654388428 seconds ---
'''
    
import time
start_time = time.time()

def num_of_cubes(a, b, c, l):
    if l == 1:
        return 2*(a*b + b*c + a*c)
    return 2*(a*b + b*c + a*c) + 4*(l - 1)*(a + b + c + l - 2)
    
def compute(goal, limit = 20000):
    C = [0]*(limit + 1)
    INF = 10**8
    for a in range(1, INF):
        if num_of_cubes(a, a, a, 1) > limit:
            break
        for b in range(a, INF):
            if num_of_cubes(a, b, a, 1) > limit:
                break
            for c in range(b, INF):
                if num_of_cubes(a, b, c, 1) > limit:
                    break
                l = 1
                while True:
                    v = num_of_cubes(a, b, c, l)
                    if v > limit:
                        break
                    C[v] += 1
                    l += 1
    
    for i, x in enumerate(C):
        if x == goal:
            return i 

if __name__ == "__main__":
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
