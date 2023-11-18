#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:09:33 2020

@author: igorvanloo
"""
'''
Project Euler Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

Anwser:
    190569291
--- 0.0005931854248046875 seconds ---    
'''

import time
from functools import cache
start_time = time.time()

def print_table(goal, alist):
    ways = [1] + [0] * (goal)
    for options in alist:
        print("Current Table " + str(ways))
        print("Current number being checked " + str(options))
        for i in range(len(ways) - options):
            print("Current i: " + str(i))
            ways[i + options] += ways[i]
        print("\n")

    return ways[-1]-1

#Method 1: partition function
def Partition(goal, alist):
    ways = [1] + [0] * (goal)
    for options in alist:
        for i in range(len(ways) - options):
            ways[i + options] += ways[i]
    return ways[-1]-1

#Method 2: generating functions
class Poly:
    def __init__(self, poly_dict):
        #Takes in poly dictionary for example {0:1, 4:1} = 1 + x^4
        self.poly_dict = poly_dict
        
    def __mul__(self, other):
        new_dict = {}
            
        for a in self.poly_dict:
            b = self.poly_dict[a]
            
            for c in other.poly_dict:
                d = other.poly_dict[c]
                
                if a + c in new_dict:
                    new_dict[a + c] += b*d
                else:
                    new_dict[a + c] = b*d
        return Poly(new_dict)
    
    def __str__(self):
        poly = ""
        for i, a in enumerate(self.poly_dict):
            b = self.poly_dict[a]
            poly += str(b) +"x^" + str(a)
            if i + 1 != len(self.poly_dict):
                poly += " + "
        return poly

def D(n, options):
    p = Poly({0:1, options[0]:-1})
    for x in options[1:]:
        p *= Poly({0:1, x:-1})
    
    rec_points = []
    for x in p.poly_dict:
        rec_points.append((x, -p.poly_dict[x]))

    @cache
    def C(n):
        if n < 0:
            return 0
        if n <= 1:
            return 1
        ans = 0
        for (a, b) in rec_points[1:]:
            ans += b*C(n - a)
        return ans
    
    return C(n)

if __name__ == "__main__":
    print(Partition(100, [x for x in range(1,101)]))
    t = time.time() - start_time
    print("--- %s seconds ---" % (time.time() - start_time))
    
    print(D(100, [x for x in range(1, 100)]))
    print("--- %s seconds ---" % (time.time() - start_time - t))