# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:32:00 2023

@author: igorvanloo
"""
'''
Project Euler Problem 647

Find (A, B) such that AT_n + B = T_x

F_3(N) = sum((A + B) where max(A, B) <= N)

T_n = n(n + 1)/2 = (n^2 + n) / 2
Look for T_{an + b} = (an + b)(an + b + 1)/2 = (a^2n^2 + 2abn + an + b^2 + b) / 2 = AT_n + B
AT_n + B = An(n + 1)/2 + B = (An^2 + An + 2B) / 2 
Therefore, comparing co-efficients, we have A = a^2, A = (2ab + a), 2B = b^2 + b
A = a(2b + 1) = a^2 => a = 2b + 1, B = (b^2 + b) / 2

for general formula see website, wrote it up nicely as I made some errors doing it in my head...

Anwser:
    563132994232918611
--- 1.9358489513397217 seconds ---
'''
import time
start_time = time.time()
    
def F(k, N):
    total = 0
    i = 1
    while True:
        
        a = 2*(k - 2)*i + 1
        b = (4 - k)*i
        
        A = pow(a, 2)
        B = ((k - 2)*b*b + (4 - k)*b)//2
        
        if max(A, B) > N:
            break
        
        total += A + B
        i += 1
    return total

def S(N):
    total = 0
    k = 3
    while True:
        t = F(k, N)
        if t == 0:
            break
        total += t
        k += 2
    return total
        
if __name__ == "__main__":
    print(S(10**12))
    print("--- %s seconds ---" % (time.time() - start_time))
