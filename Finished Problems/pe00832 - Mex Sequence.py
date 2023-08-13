# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:02:12 2023

@author: igorvanloo
"""
'''
Project Euler Problem 832

Brute force function and searched the a terms in OEIS and we get https://oeis.org/A053738
but it's not super helpful except it helped me find a pattern

Pattern 1: 
1. a = 1 now 4*a = 4
we get b = 2, a^b = 3

2. a = 4, 4*a = 16
within the next 4 turns a = [4, 5, 6, 7], b = [8, 9, 10, 11] and a^b = [12, 13, 14, 15]

3. a = 16, 4*a = 64
within the next 16 terms a = [16, ..., 31], b = [32, ..., 47], a^b = [48, ..., 63]

4. a = 64
pattern coninues

therefore M(sum_{i = 0, n} 4^i) = M(1 + 4^1 + ... + 4^n) = sum_{j = 1 to 4^(n + 1) - 1} = (4^(n + 1) - 1)(4^(n + 1))//2))

Pattern 2:

If a = 0 % 4, then b = a^b = 0 % 4
If a = 1 % 4, then b = 2 % 4, a^b = 3 % 4
If a = 2 % 4, then b = 3 % 4, a^b = 1 % 4
If a = 3 % 4, then b = 1 % 4, a^b = 2 % 4

This problem clearly has something to do with blocks of 4

1. 4^0
   a, b, a^b = 1, 2, 3, total = 6
2. 4^1
    4 8 12 24
    5 10 15 30
    6 11 13 30
    7 9 14 30
3. 4^2
    16 32 48 96
    17 34 51 102
    18 35 49 102
    19 33 50 102
    ------------
    20 40 60 120
    21 42 63 126
    22 43 61 126
    23 41 62 126
    ------------
    24 44 52 120
    25 46 55 126
    26 47 53 126
    27 45 54 126
    ------------
    28 36 56 120
    29 38 59 126
    30 39 57 126
    31 37 58 126

There is clearly a pattern here

Pattern 3:
    
Note that if 16 <= a < 16 + 4, 2*16 <= b < 2*16 + 4, 3*16 <= c < 3*16 + 4

          if 16 + 4 <= a < 16 + 2*4, 2*16 + 2*4 <= b < 2*16 + 3*4, 3*16 + 3*4 <= c < 3*16 + 4*4
          
          if 16 + 2*4 <= a < 16 + 3*4, 2*16 + 3*4 <= b < 2*16 + 4*4, 3*16 + 1*4 <= c < 3*16 + 2*4
          
          if 16 + 3*4 <= a < 16 + 4*4, 2*16 + 4 <= b < 2*16 + 2*4, 3*16 + 2*4 <= c < 3*16 + 3*4
          
This pattern continues for higher powers of 4

for example take 64 + 16 <= a < 64 + 2*16, then we have 2*64 + 2*16 <= b < 2*64 + 3*16
and 3*64 + 3*16 <= b < 3*64 + 4*16

Then we can easily find the sum of this block 
sum a = 80 + ... + 95 = 1400
sum b = 160 + ... + 175 = 2680
sum c = 240 + ... + 255 = 3960

Combine pattern 2 and 3 for a recursive solution

For example lets find M(10)

We begin with 
Let i denote the power of 4 we are on, we begin with 0

1. power = 4^i = 1
    1.1. 1 < 10 so we need to continue
    1.2. Now imagine M(10) = M'(9) where M'(9) = M(10) but the sequence starts with 
            (a, b, a^b) = (4, 8, 12) instead
    1.3. Then M(10) = M(1) + M'(9)
    1.4. i += 1

Now we find M'(9) where (a, b, a^b) = (4, 8, 12)

2. power = 4^i = 4
    2.1. 4 < 9 we continue
    2.2. Imagine M'(9) = M''(5) where the sequence begins with (a, b, a^b) = (16, 32, 48)
    2.3. Then M'(9) = M'(4) + M''(5)
    2.4. We know M'(4) = M(5) - M(1) and we can find this is because this is the block
            Where a <= 4 < 8, its sum is 114
    2.5. i += 1
    
Now we find M''(5) where (a, b, a^b) = (16, 32, 48)

3. Power = 4^i = 16
    2.1. 16 > 5 So we cannot sum the entire block, we need to subdivide the blocks and find the respective sums
    2.2. First we need to go down a power of 4, i -= 1
    2.3. We know we need to sum the block 16 <= a < 20 and just a = 20
    
Anwser:
    552839586
--- 0.0 seconds ---
'''
import time
start_time = time.time()

def mex(A):
    mex = 0
    L = len(A)
    if L == 0:
        return mex
    for mex in range(L):
        if A[mex] != mex:
            return mex
    return mex + 1

def BF(n):
    paper = [0,]
    for x in range(n):
        #print("x = ", x)
        #Step 1
        a = mex(paper)
        #print("a = ", a)
        paper.append(a)
        paper = sorted(paper)
        
        #Step 2
        b = mex(paper)
        while True:
            if b not in paper and a^b not in paper:
                break
            b += 1
        paper += [a^b, b]
        #print("<tr> <td>" + str(a) + "</td> <td>" + str(b) + "</td> <td>" +str(a^b) + "</td> <td>" + str(a + b + a^b) + "</td> </tr>")
        print(a, b, (a^b), a + b + (a^b))
        #print(a % 256, b % 256, (a^b) % 256)
        paper = sorted(paper)
        #print(paper)
    return sum(paper)

def M(n, a = 1, b = 2, c = 3, i = 0):
    mod = 10**9 + 7
    if n <= 0:
        return 0
    
    power = pow(4, i)
    if power < n:
        #M(power) + M'(n - power)
        return (M(power, a, b, c, i) + M(n - power, 4*a, 4*b, 4*c, i + 1)) % mod
    elif power == n:
        #We just need to return the sum of the block which starts at (a, b, c) and is power long
        #sum_a = (a + power) // 2 * (a + power - 1) - a * (a - 1) // 2 
        sum_a = (a + power - 1) * (a + power) // 2 - (a - 1) * a // 2 
        #sum_b = 3*power // 2 * (3*power - 1) - 2*power * (2*power - 1) // 2 
        sum_b = (b + power - 1) * (b + power) // 2 - (b - 1) * b // 2 
        #sum_c = 4*power // 2 * (4*power - 1) - 3*power * (3*power - 1) // 2 
        sum_c = (c + power - 1) * (c + power) // 2 - (c - 1) * c // 2  
        return (sum_a + sum_b + sum_c) % mod
    else:
        s_power = power // 4
        sum_1 = M(min(n, s_power), a, b, c, i - 1) % mod
        sum_2 = M(min(n - 1*s_power, s_power), a + 1*s_power, b + 2*s_power, c + 3*s_power, i - 1) % mod
        sum_3 = M(min(n - 2*s_power, s_power), a + 2*s_power, b + 3*s_power, c + 1*s_power, i - 1) % mod
        sum_4 = M(min(n - 3*s_power, s_power), a + 3*s_power, b + 1*s_power, c + 2*s_power, i - 1) % mod
        return (sum_1 + sum_2 + sum_3 + sum_4) % mod


if __name__ == "__main__":
    print(M(10**18))
    print("--- %s seconds ---" % (time.time() - start_time))
