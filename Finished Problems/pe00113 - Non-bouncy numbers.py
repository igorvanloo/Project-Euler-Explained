# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:20:01 2023

@author: igorvanloo
"""
'''
Project Euler Problem 113

Continuation of problem 112
We are dealing with 10^100 so our solution needs to be insanely efficient

My initial idea is to use dynamic programming to count the number of increasing an decreasing numbers

start with 2 empty arrays
I = [1]*9 
D = [1]*10

Then I[x] will denote the number of integers that result in an increasing number of a higher digit
D[x] is for decreasing

Note that array I has one less values because a number cannot start with 0

Now we can can calculate how many 1 digit non-bouncy numbers there are
Sum(I) = 9, Sum(D) = 10, so there are 9 increasing numbers and 10 decreasing (since it includes 0, which we need to remove)
but we have count numbers 1, 2, ..., 9 twice so final is sum(I) + Sum(D) - 1- 9 = 10 + 9 - 1 - 9 = 9

Now we recompute I and D, for example if we start with 1, we know that there are 9 choices to make an 
increasing numbers

start with 0 there are 10 increasing combinations (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
start with 1, there are 9 increasing (11, 12, 13, 14, 15, 16, 17, 18, 19)
etc
similarly for decreasing we can do the same

In short we have
I[x] = sum(I[x:]) and D[x] = sum(D[:x + 1]) we get

I = [9, 8, 7, 6, 5, 4, 3, 2, 1] 
D = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Notice sum(I) = 45, sum(D) = 55

Now we have double counted 11, 22, ... ,99 and once again we need to remove 0
so the number of 2 digit non-bouncy numbers is Sum(I) + sum(D) - 9 - 1 = 45 + 55 - 9 - 1 = 90

Together with 1 digit non-bouncy we have a total of 99

We continue this process

Notice that after each update of I and D the sum is of the previous I is I[0] and sum of previous D is D[9]

So we just sum all I[0] and D[9] and at the end remove 9*n + n for the duplicates and the 0 that is counted
in each sum of D

Anwser:
    51161058134250
--- 0.0 seconds ---
'''
import time
start_time = time.time()

def compute(n):
    I = [1]*9
    D = [1]*10
    total = 0
    for d in range(n):
        for i in range(9):
            I[i] = sum(I[i:])
            D[9 - i] = sum(D[:9 - i + 1])
        total += I[0]
        total += D[9]
    return total - 9*n - n

if __name__ == "__main__":
    print(compute(100))
    print("--- %s seconds ---" % (time.time() - start_time))
