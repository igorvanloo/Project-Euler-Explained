# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:01:03 2023

@author: igorvanloo
"""
'''
Project Euler Problem 539

https://oeis.org/A347325

Let v = n//2 = floor(n/2)

Then P(n) = 2v + 2 - 2P(v)

Furthermore note that P(2k) = P(2k + 1)

Therefore if n is even (we will be missing the n + 1 pair) we have S(n) = S(n - 1) + P(n)

Now when n is odd, we will have m = (n - 1)/2 pairs (2, 3), (4, 5), ..., (n - 1, n)

S(n) = 1 + sum_{k = 2 to n} P(k) = (P(2) + P(3)) + ... + (P(n - 1) + P(n)) = 2P(2) + ... + 2P(n - 1)
     = 1 + sum_{k = 1 to m} 2P(2k)
     = 1 + sum_{k = 1 to m} 2(2k + 2 - 2P(k))
     = 1 + 4sum_{k = 1 to m} k + 1 - sum_{k = 1 to m} 4P(k) (sum_{k = 1 to m} k + 1 = m(m + 1)/2 + m)
     = 1 + 2m(m + 1) + 4m - 4S(m)
     
Anwser:
    426334056
--- 0.0 seconds ---
'''
import time
start_time = time.time()

def bruteforce(n):
    A = [i for i in range(1, n + 1)]
    start = 1
    while len(A) != 1:
        if start % 2 == 1:
            A = [A[i] for i in range(start % 2, len(A), 2)]
        else:
            A = list(reversed([A[i] for i in range(len(A) - 2, -1, -2)]))
        #print(start % 2, A)
        start += 1
    return A

def P(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    v = n//2
    return 2*v + 2 - 2*P(v)

def S(n):
    mod = 987654321
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return (S(n - 1) + P(n)) % mod
    
    m = (n - 1)//2
    return (1 + 2*m*(m + 1) + 4*m - 4*S(m)) % mod

if __name__ == "__main__":
    print(S(10**18))
    print("--- %s seconds ---" % (time.time() - start_time))
