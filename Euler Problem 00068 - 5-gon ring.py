#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 11:25:45 2020

@author: igorvanloo
"""

'''
Project Euler Problem 68

we make a system of equations and solve in a given set a + b + c = e + c + d = b + e + f

line1 = a + b + c, then we assign d
then e = line1

very basic problem, computation time is slightly longer

Anwser:
    6531031914842725
--- 1.4682471752166748 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute_triangle():
    
    numbers = [1, 2, 3, 4, 5, 6]
    final_list = []
    for a in numbers:
        numbers_b = numbers[:]
        numbers_b.remove(a)
        for b in numbers_b:
            numbers_c = numbers_b[:]
            numbers_c.remove(b)
            for c in numbers_c:
                numbers_d = numbers_c[:]
                numbers_d.remove(c)
                for d in numbers_d:
                    numbers_e = numbers_d[:]
                    numbers_e.remove(d)
                    for e in numbers_e:
                        numbers_f = numbers_e[:]
                        numbers_f.remove(e)
                        for f in numbers_f:
                            if a + b + c == e + c + d and e + c + d == b + e + f:
                                if a < d and a < f:
                                    temp_list = [a, b, c, d, c, e, f, e, b]
                                    temp_var = "".join(str(temp_list[y]) for y in range(len(temp_list)))
                                    final_list.append(temp_var)
    return max(final_list)
               
def join_str(alist):
    temp_list = alist
    return "".join(str(temp_list[y]) for y in range(len(temp_list)))
                 
def compute():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    final_list = []
    for a in numbers:
        numbers_b = numbers[:]
        numbers_b.remove(a)
        for b in numbers_b:
            numbers_c = numbers_b[:]
            numbers_c.remove(b)
            for c in numbers_c:
                numbers_d = numbers_c[:]
                numbers_d.remove(c)
                for d in numbers_d:
                    numbers_e = numbers_d[:]
                    numbers_e.remove(d)
                    for e in numbers_e:
                        numbers_f = numbers_e[:]
                        numbers_f.remove(e)
                        for f in numbers_f:
                            numbers_g = numbers_f[:]
                            numbers_g.remove(f)
                            for g in numbers_g:
                                numbers_h = numbers_g[:]
                                numbers_h.remove(g)
                                for h in numbers_h:
                                    numbers_i = numbers_h[:]
                                    numbers_i.remove(h)
                                    for i in numbers_i:
                                        numbers_j = numbers_i[:]
                                        numbers_j.remove(i)
                                        for j in numbers_j:
                                            if a + b + c == d + c + e == f + e + g == h + g + i == j + i + b:
                                                if a < d and a < f and a < h and a < j:
                                                    temp_list = [a, b, c, d, c, e, f, e, g, h, g, i, j, i, b]
                                                    temp_var = join_str(temp_list)
                                                        
                                                    final_list.append(int(temp_var))
                            
    return (final_list)                  
        
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))