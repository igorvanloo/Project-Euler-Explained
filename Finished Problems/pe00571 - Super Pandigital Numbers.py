# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:49:35 2023

@author: igorvanloo
"""
'''
Project Euler Problem 571

Just brute force, generate all in lexographic order, first 10 is the answer

(2, 1, 7, 9, 0, 4, 11, 5, 10, 6, 3, 8) 1587937206284
(2, 3, 0, 7, 1, 8, 5, 10, 6, 4, 11, 9) 1674839888205
(3, 6, 7, 5, 2, 11, 8, 0, 4, 1, 9, 10) 2638904175622
(3, 9, 4, 0, 1, 7, 11, 8, 5, 2, 6, 10) 2806980157234
(3, 9, 5, 11, 4, 1, 2, 6, 7, 10, 8, 0) 2816957039424
(4, 5, 8, 6, 10, 11, 9, 3, 2, 7, 1, 0) 3325871906940
(5, 2, 4, 8, 3, 9, 0, 10, 7, 1, 6, 11) 3863090145827
(5, 3, 1, 8, 10, 4, 7, 9, 6, 2, 11, 0) 3909765781284
(5, 3, 4, 8, 10, 9, 11, 1, 0, 7, 6, 2) 3925260871994
(5, 3, 11, 7, 6, 2, 4, 8, 1, 10, 9, 0) 3960783529164

Anwser:
    30510390701978
--- 889.1742222309113 seconds ---
'''
import time, math, itertools
start_time = time.time()

def base_b_to_number(n, b):
    num = 0
    for x in n:
        num = b*num + x
    return num

def is_baseb_pandigital(n, b):
    if n == 0:
        return [0]
    digits = [False]*b
    while n != 0:
        digits[n % b] = True
        n //= b
    if all(digits):
        return True
    return False
    
def check_super_pandigital(n, b):
    for k in range(b - 1, 1, -1):
        if not is_baseb_pandigital(n, k):
            return False
    return True

def compute(digit):
    values = itertools.permutations(range(digit), digit)
    res = 0
    count = 10
    for x in values:
        if x[0] != 0:
            num = base_b_to_number(x, digit)
            if check_super_pandigital(num, digit):
                print(x, num)
                res += int(num)
                count -= 1
                if count == 0:
                    return res

if __name__ == "__main__":
    print(compute(12))
    print("--- %s seconds ---" % (time.time() - start_time))
