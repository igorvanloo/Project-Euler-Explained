# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:03:32 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 106

We only need to test subsets of the same size, since if they are not the same size then
condition 2 says they are not equal.

For n = 4 this gives us 3 options for a set [a, b, c, d] wher ewe use bitmask to represent (1001 = a d)

0011 vs 1100 -> Clearly 0011 > 1100 since d + c > a + b
0101 vs 1010 -> Clearly 1010 > 0101 since d > c and b > a => d + b > c + a
0110 vs 1001 -> This case we must manually test since we can't tell since d > c but b > a so it depends on if d - c > b - a

for n = 5 we have

00011 vs 01100 -> >
00011 vs 10100 -> >
00011 vs 11000 -> >
00101 vs 01010 -> >
00101 vs 10010 -> >
00101 vs 11000 -> >
00110 vs 01001 -> ?
00110 vs 10001 -> ?
00110 vs 11000 -> >
01001 vs 10010 -> >
01001 vs 10100 -> >
01010 vs 10001 -> ?
01010 vs 10100 -> >
01100 vs 10001 -> ?
01100 vs 10010 -> ?

So we should have that 5 pairs need to best tested

Now the idea becomes clear. Compare 2 strings, take the highest bit of both, mark the one with the higher bit, now if the next highest bit
indicates that the unmarked string is bigger then we run into a situation where we cannot be certain.

Answer:
    21384
--- 11.98598575592041 seconds ---
'''
import time
start_time = time.time()

def checker(A, B):
    A1 = A.index("1")
    B1 = B.index("1")
    if A1 < B1:
        flag = "A"
    else:
        flag = "B"
    A[A1] = "0"
    B[B1] = "0"
    
    while "1" in A:
        
        A1 = A.index("1")
        B1 = B.index("1")
        
        if A1 < B1:
            if flag == "B":
                return False
        else:
            if flag == "A":
                return False
        
        A[A1] = "0"
        B[B1] = "0"
    return True
    
    
def count(n):
    L = ["0"*(n - len(bin(x)[2:])) + bin(x)[2:] for x in range(pow(2, n))]
    L.pop(0)
    L.pop(-1)
    check = []
    for i, x in enumerate(L):
        for j in range(i + 1, len(L)):
            v = [x[a] != L[j][a] for a in range(n) if x[a] == "1"]
            if all(v):                
                x_count = x.count("1")
                Lj_count = L[j].count("1")
                if all([x_count == Lj_count, 1 < x_count < n//2 + 1, 1 < Lj_count < n//2 + 1]):
                    check.append([list(x), list(L[j])])
    return check

def compute(n):
    L = count(n)
    total = 0
    for A, B in L:
        if checker(A, B) == False:
            total += 1
    return total

if __name__ == "__main__":
    print(compute(12))
    print("--- %s seconds ---" % (time.time() - start_time))
