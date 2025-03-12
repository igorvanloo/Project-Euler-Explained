# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 22:53:35 2023

@author: igorvanloo
"""
'''
Project Euler Problem 795

https://oeis.org/A353909

Anwser:
    955892601606483.0
--- 220.27288222312927 seconds ---
--- 61.26275658607483 seconds --- with pypy
'''
import time, math
start_time = time.time()

def spf_sieve(N):
    #smallest prime factor sieve
    spf = [i for i in range(N + 1)]
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if spf[i] == i:
            for j in range(i*i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def divisors(pf, proper = False):
    primes = [x for x in pf]
    l = len(primes)

    def gen(n = 0):
        if n == l:
            return [1]
        else:
            pows = [1]
            p = primes[n]
            for _ in range(pf[p]):
                pows.append(pows[-1] * p)
            
            div = []
            for q in gen(n + 1):
                for p in pows:
                    div.append(q * p)
            return div
                    
    div = gen()
    if proper:
        div.pop(-1)
        return div
    return div

def G(n):
    spf = spf_sieve(n)
    
    pf_array = [{}, {}]
    for x in range(2, n + 1):
        p = spf[x]
        new_pf = {}
        curr = pf_array[x//p]
        
        for x in curr:
            new_pf[x] = curr[x]
        
        if p in new_pf:
            new_pf[p] += 1
        else:
            new_pf[p] = 1
        
        pf_array.append(new_pf)
    
    def g(n, pf):
        if n % 2 == 0:
            total = 0
            for d in divisors(pf):
                if d % 2 == 0:
                    #phi = 1
                    #core = 1
                    v = 1
                    pf_d = pf_array[d]
                    for p in pf_d:
                        e = pf_d[p]
                        #phi *= pow(p, e - 1) * (p - 1)
                        #core *= pow(p, (e - e % 2) // 2 - e)
                        v *= (p - 1) * pow(p, (e - e % 2) // 2 - 1)
                    total += v
            return n * total
        else:
            return -n
    
    return sum(g(x, pf_array[x]) for x in range(1, n + 1))

if __name__ == "__main__":
    print(G(12345678))
    print("--- %s seconds ---" % (time.time() - start_time))
