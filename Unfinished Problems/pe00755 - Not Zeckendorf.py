# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:43:45 2022

@author: IP176077
"""
'''
Project Euler Problem 755

First idea is to recursively build all combinations, then we can simply count the number of times a specific 
number is formed, but it only works up till 10^6

Lets look between fibonnaci numbers

F_1 = 1, F_2 = 2, F_3 = 3, F_4 = 5, F_5 = 8, F_6 = 13, F_7 = 21, F_8 = 34, F_9 = 55, F_10 = 89

Betwen F_1 = 1, F_2 = 2: 1 rep
Between F_2 = 2, F_3 = 3: 1 rep
Between F_3 = 3, F_4 = 5: 3 rep
Between F_4 = 5, F_5 = 8: 5 rep
Between F_5 = 8, F_6 = 13: 11 rep
Between F_6 = 13, F_7 = 21: 21 rep
Between F_7 = 21, F_8 = 34: 43 rep
Between F_8 = 34, F_9 = 55: 85 rep
Between F_9 = 8, F_10 = 13: 171 rep

We can see a pattern start with 1, then 1*2 - 1 = 1, then 1*2 + 1 = 3, then 3*2 - 1 = 5
5*2 + 1 = 11, 11*2 - 1 = 21, 21*2 + 1 = 43, etc

Let T_n = # of representations between F_n and F_(n + 1)
Then T_n = 2*T_(n - 1) - (-1)^(n - 1)


Anwser:

'''
import time, math
start_time = time.time()

def fibonnaci(n):  # Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0  # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2

def fib_till(x):
    fibnumbers = []
    n = 2
    while True:
        v = fibonnaci(n)
        if v > x:
            break
        fibnumbers.append(v)
        n += 1
    return fibnumbers

def S(n):
    fib = fib_till(n)
    #print(fib)
    l = len(fib)
    
    def representation(curr, index, struc):
        #print(curr, index, struc)
        res = {curr:[struc]}
        
        for i in range(index, l):
            v = curr + fib[i]
            s = struc + [fib[i]]
            if v > n:
                break
            #print(v, s)
            new_dict = representation(v, i + 1, s)
            for x in new_dict:
                if x in res:
                    res[x] += new_dict[x]
                else:
                    res[x] = new_dict[x]
            
        return res
    
    final = {}
    def generate(curr, index):
        if curr in final:
            final[curr] += 1
        else:
            final[curr] = 1
        
        for i in range(index, l):
            v = curr + fib[i]
            if v > n:
                break
            generate(v, i + 1)
              
    def generate2(curr, index):
        total = 1
        
        for i in range(index, l):
            v = curr + fib[i]
            if v > n:
                break
            total += generate2(v, i + 1)
        return total
    
    #generate(0, 0)
    #print(sorted([(x, final[x]) for x in final]))
    #for x in final:
    #    total += final[x]
    return generate2(0, 0)
        
if __name__ == "__main__":
    print(S(10**4))
    print("--- %s seconds ---" % (time.time() - start_time))