# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:00:02 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 185

Imagine we have a mtrix with 10n variables where n = length of code

a_00 a_01 a_02 a_03 a_04
a_10 a_11 a_12 a_13 a_14
...
a_90 a_91 a_92 a_93 a_94

Now a_ij = 1 if digit i appears in the j-th position.

For example in the solution to the first case we have 39542 so a_30 = a_91 = a_52 = a_43 = a_24 = 1, everything else is 0

This is the same as solving a set of linear equations, notably we have

for each j sum_{i = 0 to 9} a_{ij} = 1

Then we have the additional conditions based off the hints, for example 90342
a_90 + a_01 + a_32 + a_43 + a_24 = 2

Answer:
    4640261571849533
--- 0.16217970848083496 seconds ---
'''
import time
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
start_time = time.time()

example = [["90342", 2],
           ["70794", 0],
           ["39458", 2],
           ["34109", 1], 
           ["51545", 2], 
           ["12531", 1]] #39542

problem =   [["5616185650518293", 2], 
             ["3847439647293047", 1],
             ["5855462940810587", 3],
             ["9742855507068353", 3],
             ["4296849643607543", 3],
             ["3174248439465858", 1],
             ["4513559094146117", 2],
             ["7890971548908067", 3],
             ["8157356344118483", 1],
             ["2615250744386899", 2],
             ["8690095851526254", 3],
             ["6375711915077050", 1],
             ["6913859173121360", 1],
             ["6442889055042768", 2],
             ["2321386104303845", 0],
             ["2326509471271448", 2],
             ["5251583379644322", 2],
             ["1748270476758276", 3],
             ["4895722652190306", 1],
             ["3041631117224635", 3],
             ["1841236454324589", 3],
             ["2659862637316867", 2]] #4640261571849533

extra_case1 =   [['469577', 0],
                 ['427961', 1],
                 ['074058', 3],
                 ['625860', 1],
                 ['897798', 2],
                 ['229061', 1],
                 ['184109', 1],
                 ['110041', 1],
                 ['346965', 1]] #014768

extra_case2 =   [['9369335', 0],
                 ['7345939', 1],
                 ['5414729', 2],
                 ['8172959', 3],
                 ['0341379', 1],
                 ['0584086', 1],
                 ['9854139', 2],
                 ['0437064', 2],
                 ['4052852', 3],
                 ['5087169', 1],
                 ['2858907', 1],
                 ['1794039', 3]] #1452059

extra_case3 =   [['1274907331', 1], 
                 ['7861576016', 0], 
                 ['3389625019', 1], 
                 ['8657282896', 3], 
                 ['9439546289', 3], 
                 ['4601889829', 1], 
                 ['8271837850', 1], 
                 ['0710964729', 1], 
                 ['7223830712', 1], 
                 ['2160342860', 1], 
                 ['9086105385', 1], 
                 ['8815227430', 1], 
                 ['5134856041', 2], 
                 ['9205312516', 3],
                 ['6539383155', 2], 
                 ['1443839428', 1]] #9534232599

extra_case4 =   [['755214215283', 2], 
                 ['651422950188', 2], 
                 ['739646920738', 0], 
                 ['483408970908', 1], 
                 ['481052271548', 1], 
                 ['328288665274', 2], 
                 ['497206245855', 2], 
                 ['078556835952', 1], 
                 ['279888234614', 3], 
                 ['310308953665', 2], 
                 ['032488064247', 2], 
                 ['987219395661', 2], 
                 ['436289232222', 1], 
                 ['765817428137', 2], 
                 ['761363530099', 1], 
                 ['244637480673', 3], 
                 ['951088298284', 1], 
                 ['900013116089', 1], 
                 ['526362154019', 2], 
                 ['901978433932', 1], 
                 ['598213818406', 1], 
                 ['708107707295', 1], 
                 ['454878188646', 2], 
                 ['162657527857', 1]] #864482415615

def checker(guess, case):
    for y in case:
        c = 0
        curr, correct = y
        for i, x in enumerate(guess):
            if curr[i] == x:
                c += 1 
        if c != correct:
            print(curr)
            return False
    return True

def compute(case):
    n = len(case[0][0])
    num_of_conditions = n + len(case)
    M = [[0 for _ in range(10*n)] for _ in range(num_of_conditions)]
    b = [0 for _ in range(num_of_conditions)]
    
    #Add column conditions
    for j in range(n):
        for i in range(10):
            M[j][10*j + i] = 1
        b[j] = 1
            
    #Add conditions based off guesses
    for c, x in enumerate(case):
        guess, correct = x
        for i, j in enumerate(list(guess)):
            M[n + c][10*i + int(j)] = 1 
        b[n + c] = correct
    
    M = np.array(M)
    b_u = np.array(b)
    c = np.zeros_like(M[0])
    integrality = np.ones_like(c)
    constraints = LinearConstraint(M, b_u, b_u)
    bounds = Bounds(0, 1)
    res = milp(c = c, constraints = constraints, bounds = bounds, integrality = integrality)

    if res.success:
        ans = ""
        for i, x in enumerate(res.x):
            if abs(1 - x) < 10**(-8):
                ans += str(i % 10) 
    return ans

if __name__ == "__main__":
    #print(compute(example))
    print(compute(problem))
    #print(compute(extra_case1))
    #print(compute(extra_case2))
    #print(compute(extra_case3))
    #print(compute(extra_case4))
    print("--- %s seconds ---" % (time.time() - start_time))