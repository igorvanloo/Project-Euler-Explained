# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 22:18:29 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 156

https://arxiv.org/pdf/2305.10357 - Chapter 7

Answer:
    21295121502550
--- 2.6035702228546143 seconds ---
'''
import time
start_time = time.time()

def c(x, k, d):
    x1 = [int(x) for x in str(x)] + [0]
    x1 = x1[::-1]
    Y = (x//pow(10, k)) *pow(10, k - 1)
    if d > 0:
        if x1[k] > d:
            return Y + pow(10, k - 1)
        elif x1[k] == d:
            return Y + (x % pow(10, k - 1)) + 1
        else:
            return Y
    elif d == 0:
        if x1[k] > d:
            return Y
        elif x1[k] == d:
            Y - pow(10, k - 1) + (x % pow(10, k - 1)) + 1

def f(n, d):
    return sum(c(n, k, d) for k in range(1, len(str(n)) + 1))

def s(d, x = 2, p = 1):
    #Unbounded binary search
    #Start with x = 2 and p = 1
    count = 0
    values = []
    
    while True:
      upper = x + p
      
      #Cut-off limit based Section 4 periodicty remark
      if upper > d*10**10:
          return values, count
      
      v = f(x, d)
      
      #If our width is 1 and f(x + p, d) = x + p then we have found a fixed point
      #The condition below will set x to upper and p to 2, essentially restarting the process from upper
      if p == 1 and f(upper, d) == upper:
          count += 1
          values.append(upper)
      
      #If f(x, d) > x + 1, then we can skip ahead to v - 1. Set x to v - 1 and width to 1. This is covered in the last paragraph
      #after the 3 bullet points
      if v > x + 1:
        x, p = v - 1, 1
      
      #If f(upper, d) < safeleft, then we can update safeleft to x + p (= upper) and double the width
      #This covers point 1 after Lemma 7.1
      
      #Now we investigate point 3
      #If p = 1, then upper = x + 1.
      #If f(upper , d) < x we will proceed as normal since we would want range [x + 1, ..., x + 3] 
      #which when width is 1 is simply upper with width = 2*1. This covers point 3.
      elif p == 1 or f(upper, d) < x:
        x, p = upper, 2*p
      
      #If v >= safeleft, then safeleft remains the same and and we half the width
      #This covers point 2 after Lemma 7.1
      else:
        x, p = x, p//2
        
def compute():
    total = 1 #to acount for f(1, 1)
    for d in range(1, 10):
        v, c = s(d)
        print(d, c)
        total += sum(v)
    return total

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
