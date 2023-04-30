# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:26:16 2023

@author: igorvanloo
"""
'''
Project Euler Problem 822

Start with list [2, ..., n]
Take the smallest number and replace it with it's square
[2, 3, 4, 5] -> [4, 3, 4, 5] -> [4, 9, 3, 5] -> [16, 9, 4, 5]

Let S(n, m) = sum of array after m rounds
so S(5, 3) = 16 + 9 + 4 + 5 = 34
S(10, 100) = 845339386 (mod 1234567891)
Find S(10^4, 10^16) (mod 1234567891)

Reasoning:
    Investigating how to choose which number to square I notice a pattern
    [4, 3, 4, 5]                                    1, 0, 0, 0
    [4, 9, 4, 5]                                    1, 1, 0, 0
    [16, 9, 4, 5]                                   2, 1, 0, 0
    [16, 9, 16, 5]                                  2, 1, 1, 0
    [16, 9, 16, 25]                                 2, 1, 1, 1
    [16, 81, 16, 25]                                2, 2, 1, 1
    [256, 81, 16, 25]                               3, 2, 1, 1
    [256, 81, 256, 25]                              3, 2, 2, 1    
    [256, 81, 256, 625]                             3, 2, 2, 2
    [256, 6561, 256, 625]                           3, 3, 2, 2
    [65536, 6561, 256, 625]                         4, 3, 2, 2    
    [65536, 6561, 65536, 625]                       4, 3, 3, 2
    [65536, 6561, 65536, 390625]                    4, 3, 3, 3
    [65536, 43046721, 65536, 390625]                4, 4, 3, 3    
    [4294967296, 43046721, 65536, 390625]           5, 4, 3, 3   

We can see it is chosen periodically Start at 1, 0, 0, 0 (So we square first element first)
1. Square second element
2. Square first element
3. Square rest of the elements
4. Repeat steps 1-3

But this sequence breaks for S(10, 100) why?
Exponents for S(10, 17) = [3, 2, 2, 2, 2, 2, 2, 1, 1]
Exponents for S(10, 18) = [3, 3, 2, 2, 2, 2, 2, 1, 1] Notice we went up an exponent for 3 but not 9 as per
the sequence above. Why? 
Because 3^2 = 9 we need to incorporate the squares and how they change the above sequence

This Results is S(10, 100) having exponents [12, 12, 11, 11, 11, 11, 11, 11, 10] 

An important note:
    
    If our smallest number squared is larger than our largest number at any point, then we will enter a 
    cycle. 
    Let A_{n, m} be the array after m turns, now if 
    min(A_{n, m})^2 > max(A_{n, m}) => min(A_{n, m + 1})^2 > min(A_{n, m})^2 = max(A_{n, m + 1}) 
    So we need to find a value k, such that min(A_{n, k})^2 > max(A_{n, k})
    
    Work it out for S(10, 100):
    A = [2, 3, 4, 5, 6, 7, 8, 9, 10] - min(A_{10, 1}) = 2, max(A_{10, 1}) = 10
    A = [4, 3, 4, 5, 6, 7, 8, 9, 10] - min(A_{10, 2}) = 3, max(A_{10, 2}) = 10
    A = [4, 9, 4, 5, 6, 7, 8, 9, 10] - min(A_{10, 3}) = 4, max(A_{10, 3}) = 10
    We have found our k = 3 since 4^2 > 10
    
    Now we sort A = [4, 4, 5, 6, 7, 8, 9, 9, 10] where first 4 corresponds to original index 1, 2nd 4 is original index 3
    Now it is clear from here we are going to square then in this order and it will maintain this order until
    the turns run out
    
    Then divmod(n - k, n - 1) gives us the number of times the sequence is repeated and the remainder
    that is we just square every number m-k//n-1 times and then we square the first m-k % n-1 numbers again
    
    Final table of exponents is [12, 12, 11, 11, 11, 11, 11, 11, 10] as we expected

Anwser:
    950591530
--- 0.18987679481506348 seconds ---
'''
import time, math
start_time = time.time()

def BruteS(n, m):
    A = [i for i in range(2, n + 1)]
    power = [0]*(n - 1)
    for _ in range(m):
        e = min(A)
        i = A.index(e)
        A[i] = pow(e, 2)
        power[i] += 1
    return power
    
def S(n, m, mod = 1234567891):
    A = [i for i in range(2, n + 1)]
    k = 0
    while pow(min(A), 2) < max(A):
        e = min(A)
        i = A.index(e)
        A[i] = pow(e, 2)
        k += 1
        
    A = sorted(A)
    total = 0
    q, r = divmod(m - k, n - 1)
    
    for i in range(len(A)):
        if i < r:
            total += pow(A[i], pow(2, q + 1, mod - 1), mod)
        else:
            total += pow(A[i], pow(2, q, mod - 1), mod)
        
    return total % mod

if __name__ == "__main__":
    print(S(10**4, 10**16))
    print("--- %s seconds ---" % (time.time() - start_time))
