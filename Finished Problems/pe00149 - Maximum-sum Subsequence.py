# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 00:06:38 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 149

The core of the problemis called maximum subarray problem, lcukily for me 
I saw it in an assignment in University! so I've already implemented it in O(n) time

https://en.wikipedia.org/wiki/Maximum_subarray_problem#No_empty_subarrays_admitted 

Answer:
    52852124
--- 11.714919090270996 seconds ---
'''
import time
start_time = time.time()

def MaxContiguousSubarray(A):
    currMax = 0 
    currSum = 0
    for i in range(len(A)):
        currSum = max(currSum + A[i], A[i])
        currMax = max(currMax, currSum)
    return currMax

def MaxsumSubseq(M):
    currMax = 0
    l = len(M[0])
    for i in range(l):
        currMax = max(currMax,
                      MaxContiguousSubarray(M[i]), #Horizontal
                      MaxContiguousSubarray([M[j][i] for j in range(l)]), #Vertical
                      MaxContiguousSubarray([M[l - j - 1][i - j - 1] for j in range(i + 1)]), #Diagonal
                      MaxContiguousSubarray([M[i + j][i + j] for j in range(l - i)]), #Diagonal
                      MaxContiguousSubarray([M[l - j - 1][l - i + j - 1] for j in range(i + 1)]), #Anti-Diagonal
                      MaxContiguousSubarray([M[j][i - j] for j in range(i + 1)]) #Anti-Diagonal
                                            )
    return currMax

def genM():
    M = [[0 for _ in range(2000)] for _ in range(2000)]
    S = [0] + [0]*(4*10**6)

    for k in range(1, 56):
        S[k] = (100003 - 200003*k + 300007*pow(k, 3, 10**6)) % 10**6 - 500000
    
    for k in range(56, 4*10**6 + 1):
        S[k] = (S[k - 24] + S[k - 55]) % 10**6 - 500000
    
    S.pop(0)
    for i, s in enumerate(S):
        M[i//2000][i % 2000] = s
    return M

def compute():
    M = [[-2, 5, 3, 2],
         [9, -6, 5, 1],
         [3, 2, 7, 3],
         [-1, 8, -4, 8]]
    
    return MaxsumSubseq(M)

if __name__ == "__main__":
    print(MaxsumSubseq(genM()))
    print("--- %s seconds ---" % (time.time() - start_time))
