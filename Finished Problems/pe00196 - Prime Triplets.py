# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:02:51 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 193

Answer:
    322303240771079935
--- 45.744086027145386 seconds ---
'''
import time, math
start_time = time.time()
    
def prime_sieve(limit, values = True):
    result = [True] * (limit + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(limit)) + 1):
    	if result[i]:
    		for j in range(2 * i, len(result), i):
    			result[j] = False
    if values:
        return [i for (i, isprime) in enumerate(result) if isprime]
    else:
        return result
    
def prime_sieve_in_range(low_limit, upp_limit, values = True):
    primes = prime_sieve(int(math.sqrt(upp_limit)) + 1)
    result = [1 for _ in range(low_limit, upp_limit + 1)]
    for p in primes:
        S = p * (low_limit//p) - low_limit
        if S < 0:
            S += p
        for j in range(S, len(result), p):
            result[j] = 0
            
    if values:
        return [i + low_limit for (i, isprime) in enumerate(result) if isprime]
    else:
        return result
    
def S(N):
    T = (N*N + N)//2
    S = T - 3*N + 4
    E = T + 2*N + 3
    result = prime_sieve_in_range(S, E, values = False)
    
    Tri = [[(i, result[i - S]) for i in range(S, S + N - 2)],
           [(i, result[i - S]) for i in range(S + N - 2, S + 2*N - 3)],
           [(i, result[i - S]) for i in range(S + 2*N - 3, T + 1)],
           [(i, result[i - S]) for i in range(T + 1, T + N + 2)],
           [(i, result[i - S]) for i in range(T + N + 2, T + 2*N + 4)]]
        
    def search(i, row):
        prime_ng = []
        for x in range(max(0, i - 1), min(len(Tri[row - 1]), i + 1) + 1):
            for y in range(row - 1, row + 2):
                v, isvprime = Tri[y][x]
                if isvprime:
                    prime_ng.append((x, y))
        prime_ng.remove((i, row))
        return prime_ng

    total = 0
    for i, (n, isprime) in enumerate(Tri[2]):
        if isprime:
            v = search(i, 2)
            if len(v) > 1:
                total += n
            if len(v) == 1:
                j, jrow = v[0]
                if len(search(j, jrow)) > 1:
                    total += n
    return total

if __name__ == "__main__":
    print(S(5678027) + S(7208785))
    print("--- %s seconds ---" % (time.time() - start_time))
