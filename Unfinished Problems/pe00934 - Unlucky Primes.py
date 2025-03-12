# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 11:01:50 2025

@author: Igor Van loo
"""
'''
Project Euler Problem 934

Answer:

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

def count(d, N):
    if d == 2:
        k = N//2
        return k*k
    
    total = 0
    for i in range(1, d):
        #numbers of the form n = dk + i
        if i % 2 == 0:
            #We only care about even k = 2j
            #Number are of the form 2*d*j + i
            k = N//(2*d)
            
            #sum_{j = 0}^k (2*d*j + i) = 2*d*sum_{j = 1}^{k} j + i*sum_{j = 0}^k 1 = d*(k*k - k) + i*(k + 1)
            
            total += d*k*(k + 1) + i*k + i
        else:
            #We only care about odd k = 2j + 1
            #Number are of the form 2*d*j + (d + i)
            k = N//(2*d)
            
            #sum_{j = 0}^k 2*d*j + (d + i) = d*(k*k - k) + (d + i)*(k + 1)
            
            total += d*k*(k + 1) + (d + i)*k + d + i
    return total
    
def U(N):
    primes = prime_sieve(20)
    
    def u(n):
        for p in primes:
            if (n % p) % 7 != 0:
                return p
            
    totals = {p:0 for p in primes}
    mod = {i:set() for i in range(13)}
    for n in range(1, N + 1):
        v = u(n)
        if v > 10:
            print(n, v)
        totals[v] += n
        mod[n % 13].add(v)
        
    return totals, mod 

if __name__ == "__main__":
    print(U(1000))
    print("--- %s seconds ---" % (time.time() - start_time))