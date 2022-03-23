#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:04:13 2022

@author: igorvanloo
"""
'''
Project Euler Problem 247

Idea:
Recursively find squares up to a certain depth and the sort their area, similar to problem 199

The bottom left point of a square is (a, b) and its width is c
This means that (a+c, b+c) must lie on y=1/x that is b+c = 1/(a+c) => ab + (a+b)c + c^2 = 1
=> c^2 + c(a+b) +(ab - 1) = 0 => c = (-(a + b) ± √(a^2 + 2ab + b^2 - 4ab + 4))/2 = (-(a + b) ± √((a-b)^2+ 4))/2

Anwser:
    [782252, [0.0008013765943108986, [3, 3]]]
--- 3.098038911819458 seconds ---
'''
import time, math
start_time = time.time()

def find_square_width(a, b):
    cons = -(a + b)/2
    sqrt = math.sqrt((a-b)*(a-b) + 4)/2
    return cons + sqrt

def find_squares(p1, p2, left, under, depth):
    w = find_square_width(p1, p2)
    squares = [w, [left, under]]
    if depth == 1:
        return squares
    squares += find_squares(p1 + w, p2, left + 1, under, depth - 1)
    squares += find_squares(p1, p2 + w, left, under + 1, depth - 1)
    
    return squares

def compute1(depth_limit, index): #Tried to implement a recursive method but it is too slow
    squares = []
    squares.append(find_squares(1, 0, 0, 0, depth_limit))
    squares = list(reversed(sorted(squares)))
    candidates = []
    for i, elem in enumerate(squares):
        if elem[1][0] == index[0] and elem[1][1] == index[1]:
            candidates.append([i + 1, elem])
            #print(i + 1, elem)
    if len(candidates) != 0:
        return max(candidates)
    else:
        return "depth limit is too low"

def compute(min_x, index):
    squares = []
    stack = [[1, 0, 0, 0, min_x]]
    while len(stack) != 0:
        a, b, left, under, min_x = stack.pop(0)
        w = find_square_width(a, b)
        squares.append([w, [left, under]])
        if w > min_x:
            stack.append([a + w, b, left + 1, under, min_x])
            stack.append([a, b + w, left, under + 1, min_x])  
    squares = list(reversed(sorted(squares)))
    candidates = []
    for i, elem in enumerate(squares):
        if elem[1][0] == index[0] and elem[1][1] == index[1]:
            candidates.append([i + 1, elem])
            #print(i + 1, elem)
    if len(candidates) != 0:
        return max(candidates)
    else:
        return "min_x is too large"

if __name__ == "__main__":
    print(compute(0.0008, (3,3)))
    print("--- %s seconds ---" % (time.time() - start_time))