#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:10:52 2021

@author: igorvanloo
"""

'''
Project Euler Problem 345

We define the Matrix Sum of a matrix as the maximum possible sum of matrix elements such that none of the selected 
elements share the same row or column.

For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303

Not much progress here

Anwser:
    
'''

import time
start_time = time.time()


Matrix = [[  7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],
    	[627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
    	[447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
    	[217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
    	[960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
    	[870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
    	[973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
    	[322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
    	[445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
    	[414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
    	[184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
    	[821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
    	[ 34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
    	[815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
    	[813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]]

MaxMatrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def MatrixBuilder(matrix, valuestocheck):
    total = 0
    
    for x in valuestocheck:
        okayrow = False
        okaycolumn = False
        
        if sum([matrix[x[1]][i] for i in range(15)]) == 0:
                okayrow = True
        if sum([matrix[i][x[2]] for i in range(15)]) == 0:
            okaycolumn = True
        
        if okaycolumn == True and okayrow == True:
            matrix[x[1]][x[2]] = x[0]
            total += x[0]
                    
    return [total, matrix]
    
    
def compute():
    allvalues = []
    for x in range(15):
        for y in range(15):
            allvalues.append([Matrix[x][y],x,y])
    
    allvalues = sorted(allvalues)[::-1]
    
    matrices = []
    for z in range(len(allvalues)):
        MaxMatrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        MaxMatrix[allvalues[z][1]][allvalues[z][2]] = allvalues[z][0]
        temp = MatrixBuilder(MaxMatrix, allvalues[z+1:])
        matrices.append(temp)
    max_matrix = max(matrices)
    return max_matrix[0]

def IsValidMatirx(amatrix, dim):
    
    checker = []
    for x in range(dim):
        checker.append(amatrix[x].index(0))
    
    if len(set(checker)) == dim:
        return True
    return False
    
def hungarian(dim):
    temp1matrix = Matrix
    
    for row in range(dim):
        rowmax = max(temp1matrix[row])
        for y in range(dim):
            temp1matrix[row][y] -= rowmax
    
    if IsValidMatirx(temp1matrix, dim) == True:
        return temp1matrix
    else:
        print("Nope 1")
    
    temp2matrix = Matrix
            
    for column in range(dim):
        columnmax = max([temp2matrix[y][column] for y in range(dim)])
        for z in range(dim):
            temp2matrix[z][column] -= columnmax
    
    if IsValidMatirx(temp2matrix, dim) == True:
        return temp2matrix
    else:
        print("Nope 2")
        
    for column in range(dim):
        columnmax = max([temp1matrix[y][column] for y in range(dim)])
        for z in range(dim):
            temp1matrix[z][column] -= columnmax
    print(temp1matrix)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))