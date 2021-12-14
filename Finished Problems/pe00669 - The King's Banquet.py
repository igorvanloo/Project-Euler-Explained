#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 21:39:12 2021

@author: igorvanloo
"""

'''
Project Euler Problem 669

99194853094755497 is a Fibonnacci number

Built a similar algorithm as Problem 96 sudoku which I can correctly generate many seatings for

I noticed a pattern between the addition of term x and x + 1

n = 21
[21, 13, 8, 5, 16, 18, 3, 10, 11, 2, 19, 15, 6, 7, 14, 20, 1, 12, 9, 4, 17]
[34, 21, 13, 21, 34, 21, 13, 21, 13, 21, 34, 21, 13, 21, 34, 21, 13, 21, 13, 21]

n = 34                                                                                                   27
[34, 21, 13, 8,  26, 29,  5, 16, 18,  3, 31, 24, 10, 11, 23, 32,  2, 19, 15,  6, 28, 27,  7, 14, 20,  1, 33, 22, 12,  9, 25, 30, 4, 17]
[55, 34, 21, 34, 55, 34, 21, 34, 21, 34, 55, 34, 21, 34, 55, 34, 21, 34, 21, 34, 55, 34, 21, 34, 21, 34, 55, 34, 21, 34, 55, 34, 21]

Let x = F_{n+1} = 160500643816367088, y = F_{n} = 99194853094755497, z = F_{n-1} = 61305790721611591

Then they alternate between x,z and y
Let knight a be at position n
If we were currently at y then then next sum would be x or z => that the next number is x - a or z - a
if we were currently at x or z then the next sum would be y => next number is y - a 

However notice that x - a, z - a mod 99194853094755497 are the same so we are essentially swapping between
y - a and z - a in mod 99194853094755497 which is x -> -x (y - a) and x -> z - a

To find the 10,000,000,000,000,000 position we move 89,194,853,094,755,498 positions to the right
and we start at x so we apply x -> -x 44597426547377749 times and x -> z - a 44597426547377748 times alternating
which is that same as (61305790721611591 - (99194853094755497 - 44597426547377748 * 61305790721611591) % 99194853094755497)% 99194853094755497
= (44597426547377749 * 61305790721611591) % 99194853094755497
= 56342087360542122

Anwser:
    56342087360542122
--- 0.0018181800842285156 seconds ---
'''

import time, math
start_time = time.time()

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2

def Fibtill(x):
    fibnumbers = []
    n = 1
    while fibonnaci(n) <= x:
        fibnumbers.append(fibonnaci(n))
        n += 1
    return list(reversed(fibnumbers))
  
def find_poss_num(path, fib, limit):
    x = path[-1]
    options = []
    
    for y in fib:
        a = y-x
        if a <= 0:
            break
        if a <= limit:
            if a not in path:
                options.append(a)
    return options
    
def find_path(path, limit):
    fib = Fibtill(fibonnaci(len(Fibtill(2*limit + 1)) + 1))
    poss_num = find_poss_num(path, fib, limit)
    if len(path) == limit:
        return True
    if poss_num == []:
        path.pop(-1)
    else:
        for x in poss_num:
            path.append(x)            
            if find_path(path, limit) == True:
                return True
            
                path.pop(-1)
        path.pop(-1)
    return False
    
def compute(limit):
    path = [max(Fibtill(limit))]
    find_path(path, limit)
    #difference = []
    #for x in range(len(path)-1):
        #difference.append(path[x] + path[x+1])
    return path#, difference

def position(pos, limit):
    fib = Fibtill(fibonnaci(len(Fibtill(limit)) + 1))
    x = fib[0] #we never need to use it but it makes it more readable
    y = fib[1] #We always start with y
    z = fib[2]
    
    def func1(a): #a -> z - a mod y, not actually used
        return (z - a) % y
    
    def func2(a): #a -> y - a mod y = -a mod y
        return (-a) % y
    
    def func3(a, n): #both function composed give a -> a - z mod y if we repeat n times we have a -> a - z*n mod y
        return (a - z*n) % y
    
    if pos == 1:
        return y
    if pos % 2 != 0:
        mult = pos//2
        temp = func3(y, mult)
    else:
        mult = pos//2
        temp = func3(y, mult)
        temp = func2(temp)
    return temp
    
if __name__ == "__main__":
    print(compute(34))
    print(position(89194853094755498, 99194853094755497))
    print("--- %s seconds ---" % (time.time() - start_time))