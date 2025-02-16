# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:47:18 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 186

Just keep track of the connected components

Answer:
    2325629
--- 7.578438997268677 seconds ---
'''
import time
start_time = time.time()

def compute(p, number = 524287):
    S = [0]
    V = [i for i in range(10**6)]
    cc = {i:set([i]) for i in range(10**6)}
    
    k = 1
    calls = 0 
    while True:
        if k < 56:
            caller = (100003 - 200003*k + 300007*pow(k, 3, 10**6)) % 10**6 
            k += 1
            if k < 56:
                called = (100003 - 200003*k + 300007*pow(k, 3, 10**6)) % 10**6
            else:
                called = (S[k - 24] + S[k - 55]) % 10**6
            k += 1
        else:
            caller = (S[k - 24] + S[k - 55]) % 10**6
            called = (S[k - 23] + S[k - 54]) % 10**6
            k += 2
        
        S += [caller, called]
            
        if caller != called:
            
            cc_caller = V[caller]
            cc_called = V[called]
            
            if cc_caller > cc_called:
                for x in cc[cc_caller]:
                    V[x] = cc_called
                
                cc[cc_called] |= cc[cc_caller]
                del cc[cc_caller]
                
            if cc_caller < cc_called:
                for x in cc[cc_called]:
                    V[x] = cc_caller
                
                cc[cc_caller] |= cc[cc_called]
                del cc[cc_called]
            
            calls += 1
        if len(cc[V[number]]) > p*10**4 - 1:
            return calls
                
if __name__ == "__main__":
    print(compute(99))
    print("--- %s seconds ---" % (time.time() - start_time))
