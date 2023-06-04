# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:40:42 2023

@author: igorvanloo
"""
'''
Project Euler Problem 461

Standard meet in the middle algorithm

Just generate all possible e^k/n - 1, k goes up to 14211 
Then find all pairs f_n(a) + f_n(b) where a < b

for each pair, f_n(a) + f_n(b), we binary search (pi - f_n(a) + f_n(b) in pairs

Assume that f_n(a) + f_n(b) + f_n(c) + f_n(d) < pi since if it was bigger it means we have to increase values
so we would like to keep is smaller

Anwser:
    ((1433, 2147, 4903, 11363), 159820276)
--- 604.3030622005463 seconds ---
'''
import time, math
start_time = time.time()

def bisect(alist, goal):
    #Equivalent to bisect_right from bisect module
    lo = 0
    hi = len(alist)
    while lo < hi:
        mid = (lo + hi)//2
        if goal < alist[mid][0]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def f(n, k):
    return pow(math.e, k/n) - 1
    
def g(n):
    values = [0]
    k = 1
    pi = math.pi
    
    while True:
        t = f(n, k)
        if t > pi:
            break
        values.append(t)
        k += 1
    
    #print(len(values))
    pairs = []
    for i in range(len(values)):
        a = values[i]
        for j in range(i + 1, len(values)):
            b = values[j]
            t = a + b
            if t > pi:
                break
            pairs.append((a + b, i, j))
    
    pairs = sorted(pairs)
    #print(len(pairs))
    curr_min_error = 10**10
    gn = 0
    for i in range(len(pairs)):
        a = pairs[i]
        j = bisect(pairs, pi - a[0]) - 1
        b = pairs[j]
        error = math.pi - (a[0] + b[0])
        if error < curr_min_error:
            curr_min_error = error
            gn = (a[1], a[2], b[1], b[2])
    gn_sq = gn[0]*gn[0] + gn[1]*gn[1] + gn[2]*gn[2] + gn[3]*gn[3]
    return gn, gn_sq

if __name__ == "__main__":
    print(g(10000))
    print("--- %s seconds ---" % (time.time() - start_time))
