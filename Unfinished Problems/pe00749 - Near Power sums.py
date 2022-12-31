# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:25:35 2022

@author: igorvanloo
"""
'''
Project Euler Problem 749

A number, n, is a near power sum if there is a k such that the digits of n to the power k
is equal to n + 1 or n - 1

Let's say n has l digits, then the maxiumum value of its power digits is l*9^k,
What is the maximum k possible?

we want 10^l + 1 > l*9^k therefore => ln(10^l + 1 / ln(9)l) > k, therefore we have an upper bound for our k

This mean using a binary search we can can quickly find the corresponding k to check if n is a near power sum
Test cases can be checked like this

Anwser:

'''
import time, math
start_time = time.time()

def bisect(n):
    digits = intToDigit(n)
    l = len(digits)
    lo = 2
    hi = int(math.log((pow(10, l) + 1)/(math.log(9)*l)))
    while lo < hi:
        mid = (lo + hi)//2
        v = powDigits(digits, mid)
        if v == n + 1 or v == n - 1:
            return True
        if v < n + 1:
            hi = mid
        else:
            lo = mid + 1
    return False

def intToDigit(n):
    val = []
    while n != 0:
        val.append(n % 10)
        n //= 10
    return val

def powDigits(digits, k):
    return sum([pow(x, k) for x in digits])

def S(d):
    total = 0
    for x in range(1, pow(10, d)):
        if bisect(x):
            print(x)
            total += x
    return total

if __name__ == "__main__":
    print(S(6))
    print("--- %s seconds ---" % (time.time() - start_time))
