#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:49:23 2022

@author: igorvanloo
"""
'''
Project Euler Problem 316

Markov Chains, matrix state transformation

Lets say state 0 is the base state, 1 is if I get a 5, 2 is if I get a 53 and 2 is if I get 535, completed

With a probability 0.9 we will stay in state 0, 0.1 to get a 5 and move into state 1
Once we are in state 1 there is a 0.1 chance we get a 3 and move to state 2, there is a 0.1 chance we get a 5 and stay in state 1, and therefore is 0.8 chance we go back to state 0
In state 2, there is a 0.1 chance to get to state 3, and a 0.9 chance to go back to state 1

  |   0   |    1   |   2   |   3   |
0 |  0.9  |  0.1   |  0.0  |  0.0  |
1 |  0.8  |  0.1   |  0.1  |  0.0  |
2 |  0.9  |  0.0   |  0.0  |  0.1  |
3 |  0.0  |  0.0   |  0.0  |  1.0  |

p(0) = 0.9 * (1 + p(0)) + 0.1 * (1 + p(1))
p(1) = 0.8 * (1 + p(0)) + 0.1 * (1 + p(1)) + 0.1 * (1 + p(2))
p(2) = 0.9 * (1 + p(0)) + 0.1 * (1 + p(3))
p(3) = 1 * (1 + p(3))

Therefore p(3) = 0
p(2) = 0.9 + 0.9 * p(0) + 0.1 => p(2) = 1 + 0.9 * p(0)
p(1) = 1 + 0.8 * p(0) + 0.1 * p(1) + 0.1 * p(2) => 0.9 * p(1) = 1.1 + 0.89 * p(0) => p(1) = 11/9 + 8.9/9 * p(0)
p(0) = 1 + 0.9 * p(0) + 0.1 * p(1) => 0.1 * p(0) = 1 + 101/90 + 8.9/90 * p(0) =>
p(0) = 1010/90 + 89/90 * p(0) => p(0) = 1010 which is correct!

How to make this faster?

https://en.wikipedia.org/wiki/Absorbing_Markov_chain#String_generation

N = (I - P)^(-1), then t = N * [1 ,1 ,1]^T, and t[0] is the anwser

Anwser:
    542934735751917735
--- 476.2537040710449 seconds ---
'''
import time
import random
import numpy as np
from numpy.linalg import solve
start_time = time.time()

def MonteCarlo(trials, n):
    n = str(n)
    l = len(n)
    choices = [str(x) for x in range(10)]
    total = 0
    for _ in range(trials):
        guess = ""
        count = 3
        for _ in range(l):
            guess += random.choice(choices)
        if guess == n:
            total += 1
        while True:
            count += 1
            guess += random.choice(choices)
            guess = guess[1:]
            if guess == n:
                total += (count - 2)
                break
    return total/trials

def GenerateP(n):
    #Used to generate the state matrix
    n = str(n)
    l = len(n)
    matrix = []
    for i in range(l):
        #i denotes the current number we are on
        rowi = [0]*l
        #This row represents going from state i to all other states
        main = n[:i]
        next_state = n[:i+1]
        #This is what our current string looks like
        for digit in range(10):
            #We go through all the digits, and we will test them
            curr = main + str(digit)
            if curr == next_state:
                if i != l - 1:
                    rowi[i + 1] -= 1
            else:
                l2 = len(curr)
                not_found = True
                for j in range(1, l2):
                    if curr[j:] == main[:l2 - j]:
                        rowi[l2 - j] -= 1
                        not_found = False
                        break
                if not_found:
                    rowi[i - len(main)] -= 1
        rowi[i] += 10
        matrix.append(rowi)
    return matrix

def GaussJordanEliminationInteger(matrix, b):
    m, n = len(matrix), len(matrix[0]) + 1
    for x in range(m):
        matrix[x] += b[x]
    for i in range(m - 1):
        rowi = matrix[i]
        for j in range(i + 1, m):
            t = matrix[j][i]
            for k in range(n):
                matrix[j][k] -= t*rowi[k]
    for y in range(m-1, -1, -1):
        for z in range(0,y):
            for x in range(n-1, y-1, -1):
                matrix[z][x] -= matrix[y][x] * matrix[z][y]
                matrix[z][x] = round(matrix[z][x], 2)
        matrix[y][y] = round(matrix[y][y], 2)
    return matrix

def solve1(matrix, b):
    m, n = len(matrix), len(matrix[0])
    if m != len(b):
        return "Impossible to solve"
    GaussJordanEliminationInteger(matrix, b)
    return [matrix[x][n:] for x in range(m)]

def gnumpy(n):
    P = np.array(GenerateP(n))
    n = str(n)
    l = len(n)
    N = solve(P, [10]*l)
    return int(round(N[0], 3) - l + 1)
    
def g(n):
    P = GenerateP(n)
    n = str(n)
    l = len(n)
    N = solve1(P, [[10] for _ in range(l)])
    return int(N[0][0] - l + 1)
    
def compute(limit, divider):
    total = 0
    for n in range(2, limit + 1):
        if n % 10000 == 0:
            print(n)
        total += g((divider)//n)
    return total

if __name__ == "__main__":
    print(compute(999999, 10**16))
    print("--- %s seconds ---" % (time.time() - start_time))
