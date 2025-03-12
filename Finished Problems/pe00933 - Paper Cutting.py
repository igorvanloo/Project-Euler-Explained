# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:56:20 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 933

Answer:
    5707485980743099
--- 6136.293902158737 seconds --- Using Dpypy with pypy
''' 
import time
from functools import cache
start_time = time.time()

def mex(L):
    for i in range(len(L)):
        if L[i] == 0:
            return i
    return len(L)

@cache
def sG(w, h):
    if h > w:
        return sG(h, w)
    if h == 1:
        return 0
    
    vec = []
    for i in range(1, w):
        for j in range(1, h):
            TL = sG(i, j)
            TR = sG(i, h - j)
            BL = sG(w - i, j)
            BR = sG(w - i, h - j)
            
            win = TL ^ TR ^ BL ^ BR
            if win >= len(vec):
                vec += [0]*(win + 100 - len(vec))
            vec[win] = 1
    return mex(vec)

@cache
def C(w, h):
    if h > w:
        return C(h, w)
    if h == 1:
        return 0
    
    count = 0
    for i in range(1, w):
        for j in range(1, h):
            TL = sG(i, j)
            TR = sG(i, h - j)
            BL = sG(w - i, j)
            BR = sG(w - i, h - j)
            
            win = TL ^ TR ^ BL ^ BR
            if win == 0:
                count += 1
    return count
    
def D(W, H, runlength = 150):
    total = 0
    for w in range(1, W + 1):
        r = 0
        prev = -1
        run = 0
        for h in range(2, H + 1):
            curr = C(w, h)
            if prev != -1:
                if curr - prev == w - 1:
                    run += 1
                else:
                    run = 0
            prev = curr
            if run < runlength:
                r += curr 
            else:
                r += (w - 1)*((H - h)*(H - h + 1))//2 + (H - h + 1)*curr
                break
        total += r
        print("w = ", w, "150 run length found at h = ", h)
    return total

def Dpypy(W, H, runlength = 150):
    total = 0
    sG_cache = [[-1 for _ in range(H + 1)] for _ in range(W + 1)]
    
    def sG(w, h):
        
        if h < 2 or w < 2:
            sG_cache[w][h] = 0
            return 0
        
        if sG_cache[w][h] != -1:
            return sG_cache[w][h]
        
        vec = []
        for i in range(1, w):
            for j in range(1, h):
                TL = sG(min(i, j), max(i, j))
                TR = sG(min(i, h - j), max(i, h - j))
                BL = sG(min(w - i, j), max(w - i, j))
                BR = sG(min(w - i, h - j), max(w - i, h - j))
                
                win = TL ^ TR ^ BL ^ BR
                if win >= len(vec):
                    vec += [0]*(win + 100 - len(vec))
                vec[win] = 1
        sG_cache[w][h] = mex(vec)
        return sG_cache[w][h]

    def C(w, h):
        count = 0
        for i in range(1, w):
            for j in range(1, h):
                TL = sG(min(i, j), max(i, j))
                TR = sG(min(i, h - j), max(i, h - j))
                BL = sG(min(w - i, j), max(w - i, j))
                BR = sG(min(w - i, h - j), max(w - i, h - j))
                
                win = TL ^ TR ^ BL ^ BR
                if win == 0:
                    count += 1
        return count
    
    for w in range(1, W + 1):
        t = 0
        prev = -1
        run = 0
        for h in range(2, H + 1):
            curr = C(w, h)
            if prev != -1:
                if curr - prev == w - 1:
                    run += 1
                else:
                    run = 0
            prev = curr
            if run < runlength:
                t += curr 
            else:
                t += (w - 1)*((H - h)*(H - h + 1))//2 + (H - h + 1)*curr
                break
        total += t
        print("w = ", w, "150 run length found at h = ", h)
    return total

if __name__ == "__main__":
    print(Dpypy(123, 1234567))
    print("--- %s seconds ---" % (time.time() - start_time))
