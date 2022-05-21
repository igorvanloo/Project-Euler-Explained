#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:59:16 2022

@author: igorvanloo
"""
'''
Project Euler Problem 

First notice that if we have x$

if we get a heads then tails we have x*(1 + 2f)*(1 - f)
If we get a tails then heads we have x*(1 - f)*(1 + 2f)
Essentially it doesn't matter in with order we win
Therefore our total winnings afetr the game is (1 + 2f)^h(1 - f)^(1000-h), where h represents the number of heads we got

My function find_f() confirms wolframalpha value f ≈ 0.146883922440941..., which would take 431.26 heads to reach a billion

we need atleast 432 heads to reach one billion therefore the solution is sum h = 432 to 1000 of 1000Ch/2^1000

Anwser:
    0.999992836187
--- 0.05437779426574707 seconds ---
'''
import time, math
start_time = time.time()

def winnings(x, f):
    return pow(1 + 2*f, x) * pow(1 - f, 1000 - x)
    
def find_f():
    f = 0.001
    goal = 10**9
    step = 0.001
    best_f, corresponding_x = 0, 1000
    
    while f < 0.5:
        x = 1
        while winnings(x, f) < goal:
            x += 1
        if x < corresponding_x:
            best_f, corresponding_x = f, x
        f += step
    return best_f, corresponding_x

def n_choose_r(n, r):  # nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
    
def compute():
    total = 0
    for h in range(432, 1001):
        total += n_choose_r(1000, h)
    return round(total/pow(2, 1000), 12)
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
