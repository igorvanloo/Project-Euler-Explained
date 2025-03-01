# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:28:21 2025

@author: Igor van Loo
"""
'''
Project Euler Problem 237

Brute force first few values
T(1) = 1
T(2) = 1
T(3) = 4
T(4) = 8
T(5) = 23

Leads us to https://oeis.org/A181688

T(n) = 2T(n - 1) + 2T(n - 2) - 2T(n - 3) + T(n - 4) n >= 4

From here we can just use matrix exponentiation

Let X = [[2, 2, -2, 1],
         [1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0]]

Let T_n = [T(n),
           T(n - 1),
           T(n - 2),
           T(n - 3)]

Then we have T_{n + 1} = X * T_n

Therefore T_{10**12} = X^(10**12 - 4)T_4

Answer:
    15836928
--- 0.0010030269622802734 seconds ---
'''
import time
start_time = time.time()

def fillmatrix(size, val = 0):
    if type(size) != tuple:
        return "Size must be a tuple"
    return [[val]*size[1] for _ in range(size[0])]

def matrix_mul(A, B, mod):
    if type(A) != list or type(B) != list:
        return "A and B must be lists"
    m1, n1 = len(A), len(A[0])
    m2, n2 = len(B), len(B[0])
    if n1 != m2:
        return "Cannot multiply matrices"
    matrix = fillmatrix((m1, n2))
    for row in range(m1): 
        for col in range(n2):
            for elt in range(len(B)):
              matrix[row][col] += A[row][elt] * B[elt][col]
              matrix[row][col] %= mod
    return matrix

def matrix_pow(A, n, mod):
    A_res = A
    for bit in bin(n)[3:]:
        A_res = matrix_mul(A_res, A_res, mod)
        if bit == "1":
            A_res = matrix_mul(A_res, A, mod)
    return A_res

def T(n):
    mod = 10**8
    T = [[8], [4], [1], [1]]
    X = [[2, 2, -2, 1],
         [1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0]]
    
    if n < 5:
        return T[4 - n][0]
    
    P = matrix_pow(X, n - 4, mod)
    PT = matrix_mul(P, T, mod)
    return PT[0][0]

if __name__ == "__main__":
    print(T(10**12))
    print("--- %s seconds ---" % (time.time() - start_time))
