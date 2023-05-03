# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:15:14 2023

@author: igorvanloo
"""
'''
Project Euler Problem 93

take code from problem 828

Anwser:
    1258
--- 0.07101058959960938 seconds ---
'''
import time, itertools
from functools import lru_cache
start_time = time.time()

@lru_cache(maxsize = 10**5)
def recursiveGenerate(A):
    values = set()
    if len(A) == 1:
        values.add(A[0])
        return values
    
    multiplesFlag = False
    for x in A:
        if A.count(x) > 1:
            multiplesFlag = True
        
    for k in range(1, len(A)):
        
        combs1 = [y for y in itertools.combinations(A, k)]
        combs2 = [y for y in itertools.combinations(A, len(A) - k)]
        
        for i in range(len(combs1)):
            for j in range(len(combs2)):
                
                t = set(combs1[i]).intersection(set(combs2[j]))
                flag = False
                if len(t) == 0:
                    flag = True
                else:
                    if multiplesFlag:
                        flag = True
                        for x in t:
                            xcount = combs1[i].count(x) + combs2[j].count(x)
                            if xcount > A.count(x):
                                flag = False
                if flag:
                    t1 = recursiveGenerate(combs1[i])
                    t2 = recursiveGenerate(combs2[j])
                    for v1 in t1:
                        for v2 in t2:
                            values.add(v1 + v2)
                            values.add(v1 * v2)
                            if v1 - v2 > 0:
                                values.add(v1 - v2)
                            values.add(v1 / v2)
    return values

def compute():
    maxConsecutive = 0
    ans = None
    for d in range(4,10):
        for c in range(3, d):
            for b in range(2, c):
                for a in range(1, b):
                    values = sorted([int(x) for x in recursiveGenerate((a,b,c,d)) if int(x) == float(x)])
                    for i, x in enumerate(values):
                        if i + 1 != x:
                            maxCurrConsecutive = i
                            currAns = (a, b, c, d)
                            break
                #print((a,b,c,d), maxCurrConsecutive)
                if maxCurrConsecutive > maxConsecutive:
                    maxConsecutive = maxCurrConsecutive
                    ans = currAns
    print(maxConsecutive)
    return "".join(str(x) for x in ans)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
