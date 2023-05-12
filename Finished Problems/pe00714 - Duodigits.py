# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:35:02 2023

@author: igorvanloo
"""
'''
Project Euler Problem 714

Suppose we have a number n
Let A = {1, 11, ..., 11..11 (n times), 11..111 (n + 1 times)}

Now for x in A do x (mod n)
Since A has n + 1 elements there will be wto elements in A such that x1 = x2 (mod n) (x1 > x2)
=> x1 - x2 = 0 (mod n) and then x1 - x2 = 1111..000 and it is divisible by n
That is x1 - x2 is a duodigit multiple of n consisting of only 1's and 0's

Anwser:
    245276777556527592946
--- 176.1213300228119 seconds ---
'''
import time, math
start_time = time.time()

def d(x):
    curr = x
    while len(set(str(curr))) > 2:
        curr += x
    return curr

def D1(k):
    total = 0
    for n in range(1, k + 1):
        t = d(n)
        print(n, t)
        total += t
    return sum(d(n) for n in range(1, k + 1))

def genDuoDigits(d, x, y):
    duodigits = set()
    combs = {0}
    
    for _ in range(d):
        temp = []
        for v in combs:
            for z in [x, y]:
                t = v*10 + z
                if t != 0:
                    temp.append(t)
                    duodigits.add(t)
        combs = temp
    
    return duodigits

def D(n):
    INF = math.inf
    d = [INF]*(n + 1)
    d[0] = 0
    duodigits = set()
    duodigitsspecial = set()
    
    for x in range(0, 10):
        for y in range(x + 1, 10):
            if x == 0:
                duodigitsspecial = duodigitsspecial.union(genDuoDigits(21, x, y))
            duodigits = duodigits.union(genDuoDigits(15, x, y))
    duodigits = sorted(duodigits)
    duodigitsspecial = sorted(duodigitsspecial)
    
    for n in range(1, len(d)):
        if n % 10 == 0:
            for dds in duodigitsspecial:
                if dds % n == 0:
                    d[n] = dds
                    break
        else:
            for dd in duodigits:
                if dd % n == 0:
                    d[n] = dd
                    break
        
    return sum([d[x] for x in range(len(d)) if d[x] != INF])

if __name__ == "__main__":
    print(D(50000))
    print("--- %s seconds ---" % (time.time() - start_time))
