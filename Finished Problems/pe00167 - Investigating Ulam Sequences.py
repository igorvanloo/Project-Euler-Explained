# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 23:31:45 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 167

S. R. Finch, Patterns in 1-additive sequences, Experimental Mathematics 1 (1992), 57-63.
 
Answer:
    3916160068885
--- 5.362151384353638 seconds ---
'''
import time
start_time = time.time()

def delta(x):
    if x == 0:
        return 1
    return 0 

def Ulam(v, t):
    # See S. R. Finch, Patterns in 1-additive sequences, Experimental Mathematics 1 (1992), 57-63.
    a = 2
    e2 = 2*v + 2
    u = [a] + [x for x in range(v, e2, 2)] + [e2]
    b = [0]
    for x in range(3, e2, 2):
        if x in u:
            b.append(1)
        else:
            b.append(0)

    n = (e2 - 1)//2 + 1
    cs = None
    while True:
        curr = 2*n + 1
        bn = delta(b[n - 1] - 1) + delta(b[n - v - 1] - 1)
        
        if bn == 1:
            u.append(curr)
            
            if u[-1] - u[-2] == e2:
                #We have reached the periodic point
                if cs == None:
                    cs = len(u) - 2
                else:
                    ce = len(u) - 2
                    break
            
        b.append(bn)
        n += 1
    if t < ce:
        return u[t]
    
    p = ce - cs #period length
    diff = u[ce] - u[cs]
    
    return (t - cs)//p * diff + u[(t - cs) % p + cs - 1], p

def compute():
    total = 0 
    for n in range(2, 11):
        t, p = Ulam(2*n + 1, 10**11)
        print(t, p)
        total += t
    return total
        
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))