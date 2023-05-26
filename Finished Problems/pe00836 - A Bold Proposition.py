# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:32:02 2023

@author: igorvanloo
"""
'''
Project Euler Problem 836

Extremely difficult, do not attempt under any cost.

Anwser:
    aprilfoolsjoke
--- 0.0 seconds ---
'''
import time, math
start_time = time.time()

def f(m, p):
    line1 = '<p>Let $A$ be an <b>affine plane</b> over a <b>radically integral local field</b> $F$ with residual characteristic $p$.</p>'
    line2 = '<p>We consider an <b>open oriented line section</b> $U$ of $A$ with normalized Haar measure $m$.</p>'
    line3 = '<p>Define $f(m, p)$ as the maximal possible discriminant of the <b>jacobian</b> associated to the <b>orthogonal kernel embedding</b> of $U$ <span style="white-space:nowrap;">into $A$.</span></p>'
    line4 = '<p>Find $f(20230401, 57)$. Give as your answer the concatenation of the first letters of each bolded word.</p>'
    text = line1 + line2 + line3 + line4
    
    ans = ""
    
    start = 0
    end = -1
    for x in range(len(text) - 4):
        if text[x:x+3] == '<b>':
            start = x + 3
        if text[x:x+4] == '</b>':
            end = x
        
        if start < end:
            words = text[start:end].split()
            for w in words:
                ans += w[0]
            start = 0
            end = -1
    
    return ans
            
if __name__ == "__main__":
    print(f(20230401, 57))
    print("--- %s seconds ---" % (time.time() - start_time))
