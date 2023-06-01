# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:56:16 2023

@author: igorvanloo
"""
'''
Project Euler Problem 655

Let 1 <= x <= 99999

let x = a*10^4 + b*10^3 + c*10^2 + d*10 + e

now a = reversed(e), b = rev(d)

x_1 = a*10^4 + e
x_2 = b*10^3 + c*10^2 + d*10

now we go through 1 <= a <= 9 and we find x_1 % 109
and 1 <= b <= 9, 1<= c <= 9 and we find x_2 % 109

then we want all pairs (x_1, x_2) such that x_1 + x_2 = 0 (mod 109) similar for other values of N

n = 2 a|b
n = 3 a|b|a
n = 4 a|b|b|a
n = 5 a|b|c|b|a
n = 6 aa|b|b|aa
n = 7 aa|b|c|b|aa
n = 8 aa|bb|bb|aa
n = 9 aa|bb|c|bb|aa

8 0
9 0
10 0
11 0
12 0
13 0
14 0
15 0
16 8
17 91
18 101
19 924
20 711
21 8956
22 8974
23 89916
24 90410
25 900228
26 900402
27 8999724
28 9000685
29 89998696
30 89992744
31 900011069
32 900004693

Anwser:
    2000008332
--- 1899.9521100521088 seconds ---
'''
import time, math
start_time = time.time()

def rev(x, l):
    new_x = 0
    for _ in range(l):
        r = x % 10
        x //= 10
        new_x *= 10
        new_x += r
    return new_x

def gen(N, mod):
    if N == 2:
        count = 0
        for x in range(1, 100):
            if x // 10 == x % 10:
                if x % mod == 0:
                    count += 1
                    #print(x)
        return count
    
    if N == 3:
        count = 0
        for x in range(1, 1000):
            if x // 100 == x % 10:
                if x % mod == 0:
                    count += 1
                    #print(x)
        return count
    
    x_1_v = {}
    x_2_v = {}
    
    if N % 2 == 0:    
        for a in range(pow(10, N//2 - N//4)):
            if a >= pow(10, N//2 - N//4 - 1):
                x_1 = (a * pow(10, (N - math.ceil(N/4))) + rev(a, N//2 - N//4)) % mod
                if x_1 in x_1_v:
                    x_1_v[x_1] += 1
                else:
                    x_1_v[x_1] = 1
            if a < pow(10, N//4):
                x_2 = (rev(a, N//4) * pow(10, N//2) + a * pow(10, N//2 - N//4)) % mod
                if x_2 in x_2_v:
                    x_2_v[x_2] += 1
                else:
                    x_2_v[x_2] = 1
    else:
        for a in range(pow(10, N//2 - N//4)):
            if a >= pow(10, N//2 - N//4 - 1):
                t = a * pow(10, (N - round(N/4))) + rev(a, N//2 - N//4)
                x_1 = t % mod
                if x_1 in x_1_v:
                    x_1_v[x_1] += 1
                else:
                    x_1_v[x_1] = 1
                
            if a < pow(10, N//4):
                for c in range(10):
                    t = rev(a, N//4) * pow(10, N//2 + 1) + c * pow(10, N//2) + a * pow(10, N//2 - N//4)
                    x_2 = t % mod
                    if x_2 in x_2_v:
                        x_2_v[x_2] += 1
                    else:
                        x_2_v[x_2] = 1
                    
    count = 0
    for x in x_1_v:
        t = (mod - x) % mod
        if t in x_2_v:
            count += x_1_v[x]*x_2_v[t]
    return count

def compute(N, mod):
    count = 0
    for x in range(len(str(mod)), N + 1):
        t = gen(x, mod)
        print(x, t)
        count += t
    return count
    
if __name__ == "__main__":
    #print(compute(5, 109))
    print(compute(32, 10**7 + 19))
    print("--- %s seconds ---" % (time.time() - start_time))
