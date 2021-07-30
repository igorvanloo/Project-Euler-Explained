#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 21:52:53 2021

@author: igorvanloo
"""

'''
Project Euler Problem 86

Imagine an AxBxC cuboid where A >= B >= C, now we unfold the cuboid


           |F - - - -| 
           |- - - - -|
           |- - - - -| 3x5
6x3             
|F - -|    |- - - - -| 6x5
|- - -|    |- - - - -|
|- - -|    |- - - - -|
|- - -|    |- - - - -|
|- - -|    |- - - - -|
|- - -|    |- - - - S|

The distance from S to F is sqrt(A^2 + (B+C)^2)

So we need to find all integer solutions of d = sqrt(A^2 + (B+C)^2) where M >= A >= B >= C

We can generate pythagorean triples to find all the valid triangles, m^2 + n^2 is the hypotenuse
and we know that it will be an integer, therefore this solves the above problem however we must account for combinations

Case 1: let A = 2mn and (B+C) = m^2 - n^2 

Case 2: let A = m^2 - n^2 and B+C = 2mn

Now if A > B+C, then we need to find all combinations of B,C that are valid that is B >= C

if B+C = 5 for example we could have (B,C) = (4,1) or (3,2)
if B+C = 6 for example we could have (B,C) = (5,1) or (4,2) or (3,3) there will always be floor((B+C)/2) combinations

If B+C > A
We check if B+C > 2A => B or C > A which is impossible so there are 0 situations

otherwise we Have that A >= B >= C

B+C = 12 A = 9 then (A,B,C) = (9,9,3) or (9,8,4) or (9,7,5) or (9,6,6) 4 possibilities
B+C = 15 A = 8 then (A,B,C) = (8,8,7)
B+C = 16 A = 8 then (A,B,C) = (8,8,8)

Anwser:
    1818
--- 0.024382829666137695 seconds ---
'''

import time, math

def combinations(a, bc):
    if 2*a < bc:
        return 0
    elif a >= bc:
        return (bc//2)
    else:
        if bc % 2 == 0:
            return a + 1 - ((bc)//2)
        else:
            return a - ((bc-1)//2)
    
def ppt(limit): #Pythagorean Triplet generator
    triples = [0]*(limit + 1)
    for m in range(1,int(math.sqrt(2*limit))+1):
        for n in range(1,m):
            if (m+n) % 2 == 1 and math.gcd(m,n) == 1:
                #a = m**2 + n**2 #not needed for this problem
                b = m**2 - n**2
                c = 2*m*n
                #Case 1
                for k in range(1, int(limit/b) + 1):
                    triples[k*b] += combinations(k*b, k*c)
                
                #Case 2 
                for k in range(1, int(limit/c) + 1):
                    triples[k*c] += combinations(k*c, k*b)
    
    #return sum(triples[:101])

    total = 0
    for x in range(len(triples)):
        total += triples[x]
        if total > 10**6:
            return x

if __name__ == "__main__":
    start_time = time.time()
    print(ppt(10000))
    print("--- %s seconds ---" % (time.time() - start_time))