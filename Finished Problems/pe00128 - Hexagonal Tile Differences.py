# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:49:44 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 128

Answer:
    14516824220
--- 0.4499776363372803 seconds ---
'''
import time, math
start_time = time.time()

def is_prime(x):  # Test if giving value is a prime
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True
    
def pos(i, k, r):
    return 2 + 6*math.comb(i, 2) + i*k + r
    
def PD(n):
    i = 1
    v = math.comb(2, 2)
    while True:
        v1 = 1 + 6*math.comb(i + 1, 2)
        if v1 >= n:
            break
        else:
            v = v1
            i += 1
    j = n - v - 1
    k, r = j//i, j % i

    #print("Pos: ", pos(i, k, r))
    
    v0 = 1 + 6*math.comb(i - 1, 2)

    if r == 0:
        if k == 0:
            nb = [v + j + 2, v1]
            nb += [v1 + (i + 1)*k + 1, v1 + (i + 1)*k + 2, v1 + 6*(i + 1)]
        else:
            nb = [v + j, v + j + 2]
            nb += [v1 + (i + 1)*k, v1 + (i + 1)*k + 1, v1 + (i + 1)*k + 2]
        nb += [v0 + (i - 1)*k + 1]
    else:
        if k == 5 and r == i - 1:
            nb = [v + j, v]
            nb += [v0 + (i - 1)*k + r + 1, v0 + 1]

        else:
            nb = [v + j, v + j + 2]
            nb += [v0 + (i - 1)*k + r + 1, v0 + (i - 1)*k + r]
        nb += [v1 + (i + 1)*k + r + 1, v1 + (i + 1)*k + r + 2]
    #print(nb)
    return [abs(n - x) for x in nb]

def compute(n):
    L = [1, 2] #PD(1) = 3, PD(2) = 3
    i = 2
    v = 7
    while len(L) < n + 1:
        if is_prime(6*i - 1):
            if is_prime(6*i + 1):
                if is_prime(12*i + 5):
                    L.append(v + 1)
            
            if is_prime(6*i + 5):
                if is_prime(12*i - 7):
                    L.append(1 + 6*math.comb(i + 1, 2))
        i += 1     
        v = 1 + 6*math.comb(i, 2)
        
    return L[n - 1]

if __name__ == "__main__":
    print(compute(2000))
    print("--- %s seconds ---" % (time.time() - start_time))
