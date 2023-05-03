# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 22:51:14 2023

@author: igorvanloo
"""
'''
Project Euler Problem 828 

I have a correct algorithm based on https://codinghelmet.com/exercises/expression-from-numbers
I modified it to python and to suit the problem better, however it is extremely slow.

Modified it to become recursive and used cache to greatly speed it up

Anwser:
    148693670
--- 7.787013530731201 seconds ---
'''
import time, itertools
from functools import lru_cache

start_time = time.time()

def ReadFile():  # Create the inital list
    file = open("C:/Users/IP176077/Dropbox/PC/Desktop/Python-Projects/Project-Euler-Related/0. Project Euler Files/p828_number_challenges.txt")
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        x = x.rstrip()
        x += ","
        v = int(x[:3])
        n = []
        t = 4
        for i, k in enumerate(x[4:]):
            if k == ",":
                n.append(int(x[t:4 + i]))
                t = 4 + i + 1
        datalist.append((v, n))
    return datalist

class P:
    def __init__(self, value, mask, left, right, operation):
        self.value = value
        self.mask = mask
        self.left = left
        self.right = right
        self.operation = operation
        
        if self.left == None and self.right == None:
            self.expression = str(value)
        else:
            self.expression = "(" + self.left.expression + self.operation + self.right.expression + ")"
            
def generateExpressions(g, A):
    values = [(x, "0"*i + "1") for i, x in enumerate(A)]
    E = [P(x, "1" + "0"*i, None, None, None) for i, x in enumerate(A)]
    Q = [P(x, "1" + "0"*i, None, None, None) for i, x in enumerate(A)]
    goal = []
    
    while Q != []:
        a = Q.pop(0)
        if a.value == g:
            print(a.expression)
            goal.append(a)
            
        for b in E:
            if bin(int(a.mask, 2) & int(b.mask, 2))[2:] == "0": #We have not used a number twice
                newmask = bin(int(a.mask, 2) | int(b.mask, 2))[2:]
                
                #Addition
                c = P(a.value + b.value, newmask, a, b, "+")
                if (c.value, c.mask) not in values:
                    values.append((c.value, c.mask))
                    Q.append(c)
                    E.append(c)
                
                #Subtraction
                if a.value - b.value > 0:
                    c = P(a.value - b.value, newmask, a, b, "-")
                    if (c.value, c.mask) not in values:
                        values.append((c.value, c.mask))
                        Q.append(c)
                        E.append(c)
                
                #Multiplication
                c = P(a.value * b.value, newmask, a, b, "*")
                if (c.value, c.mask) not in values:
                    values.append((c.value, c.mask))
                    Q.append(c)
                    E.append(c)
                
                #Division
                if a.value % b.value == 0:
                    c = P(a.value // b.value, newmask, a, b, "/")
                    if (c.value, c.mask) not in values:
                        values.append((c.value, c.mask))
                        Q.append(c)
                        E.append(c)
                
    if goal == []:
        return 0
    
    v = []
    for x in goal:
        total = 0
        for i, y in enumerate(x.mask[::-1]):
            if y == "1":
                total += A[i]
        v.append(total)
    return min(v)

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
                            if v1 % v2 == 0:
                                values.add(v1 // v2)
    return values
    
def compute():
    data = ReadFile()
    total = 0
    mod = 1005075251
    for n, (g, A) in enumerate(data):
        s = []
        for k in range(1, len(A) + 1):
            combs = itertools.combinations(A, k)
            for x in combs:
                if g in recursiveGenerate(x):
                    s.append(sum(x))
        if len(s) == 0:
            s = 0
        else:
            s = min(s)
        print(n + 1, s)
        total += pow(3, n + 1, mod) * s
    return total % mod

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
