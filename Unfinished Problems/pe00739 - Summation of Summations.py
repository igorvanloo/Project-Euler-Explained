# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:44:42 2023

@author: igorvanloo
"""
'''
Project Euler Problem 739

If we start with [1, 1, ...]
f(n) = https://oeis.org/A000108


Anwser:

'''
import time, math
start_time = time.time()

def lucas(n):
    a0 = 1
    a1 = 3
    seq = [a0, a1]
    for _ in range(n - 2):
        a2 = a1 + a0
        a0 = a1
        a1 = a2
        seq.append(a2)
    return seq
    
def f(x):
    mod = 10**9 + 7
    #seq = lucas(x)
    seq = [1]*x
    res = [seq[0]]
    for _ in range(len(seq) - 1):
        #print(seq)
        new_seq = [seq[1]]
        for j in range(2, len(seq)):
            new_seq.append(seq[j] + new_seq[j - 2])
        seq = new_seq
        res.append(seq[0])
    return res

if __name__ == "__main__":
    print(f(20))
    print("--- %s seconds ---" % (time.time() - start_time))
