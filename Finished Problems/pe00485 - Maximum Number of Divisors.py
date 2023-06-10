# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:31:52 2023

@author: IP176077
"""
'''
Project Euler Problem 485

d(n) = # of divisors of n
M(n, k) = max d(j) for n <= j <= n + k - 1
S(u, k) = sum(M(n, k)) for 1 <= n <= u - k + 1
S(1000, 10) = 17176 

precalculate smallest prime factor, which is then used to get prime factorisation

create an array containing all d(n), then solve "sliding window problem" to find M(n, k)

I do it by comparing new_element in a bit of a brute force way

Anwser:
    51281274340
--- 86.31504249572754 seconds ---
'''
import time, math
start_time = time.time()

def spf_sieve(N):
    spf = [i for i in range(N + 1)]
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if spf[i] == i:
            for j in range(i*i, N + 1, i):
                spf[j] = i
    return spf

def S_original(u, k):
    spf = spf_sieve(u + 2)
    print("spf sieve done")
    print("--- %s seconds ---" % (time.time() - start_time))
    def d(n):
        total = 1
        while n != 1:
            p = spf[n]
            c = 1
            while n % p == 0:
                c += 1
                n //= p
            total *= c
        return total
            
    d_array = [0] + [d(i) for i in range(1, u + 2)]
    print("d_array precalculated")
    print("--- %s seconds ---" % (time.time() - start_time))
    
    curr_dict = {}
    for x in d_array[1:1 + k]:
        if x in curr_dict:
            curr_dict[x] += 1
        else:
            curr_dict[x] = 1
            
    total = 0
    for i in range(1, u - k + 2):
        if i % 10**6 == 0:
            print(i)
            
        t = max(curr_dict)
        prev_elem = d_array[i]
        
        curr_dict[prev_elem] -= 1
        if curr_dict[prev_elem] == 0:
            del curr_dict[prev_elem]
        
        next_elem = d_array[i + k]
        if next_elem in curr_dict:
            curr_dict[next_elem] += 1
        else:
            curr_dict[next_elem] = 1
        
        total += t
    return total
    
def S(u, k):
    spf = spf_sieve(u + 1)
    print("spf sieve done")
    d = spf
    for i in range(2, u + 2):
        if spf[i] == i:
            d[i] = 2
        else:
            #We use the fact that d[n] = (e + 1) * d[n/p^e]
            p = spf[i]
            t = i // p
            e = 2
            while t % p == 0:
                e += 1
                t //= p
            d[i] = d[t]*e
    print("d has been calculated")
    
    window = {}
    for x in d[1:1 + k]:
        if x in window:
            window[x] += 1
        else:
            window[x] = 1
            
    m = max(window)
    total = m
    for i in range(1, u - k + 1):
        flag = False
        outgoing = d[i]
        window[outgoing] -= 1
        if window[outgoing] == 0:
            flag = True
            del window[outgoing]
        
        incoming = d[i + k]
        if incoming in window:
            window[incoming] += 1
        else:
            window[incoming] = 1
        
        if incoming > m:
            m = incoming
        elif outgoing == m:
            if flag:
                m = max(window)
        
        total += m
                
    return total

if __name__ == "__main__":
    print(S(10**8, 10**5))
    print("--- %s seconds ---" % (time.time() - start_time))
