# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:25:29 2023

@author: IP176077
"""
'''
Project Euler Problem 733

a_i = 153^i (mod 10^7 + 9)

process each element in order in a dictionary
n = 0, 153 dict = {153: None}
n = 1, 23409 > 153 dict = {153: 23409, 23409: None}
n = 2, 3581577 > 23409 dict = {153: [23409, 3581577], 23409: [3581577], 3581577: []}
n = 3, 7980255 > 3581577 dict = {153: [23409, 3581577, 7980255], 23409: [3581577, 7980255], 3581577: [7980255], 7980255: []}
n = 5, 976697 < 7980255
              < 3581577
              > 23409
    dict = {153: [23409, 3581577, 7980255, 976697], 23409: [3581577, 7980255, 976697], 3581577: [7980255], 7980255: []}
n = 6, 9434375 > 7980255
dict = {153: [23409, 3581577, 7980255, 976697, 9434375], 23409: [3581577, 7980255, 976697, 9434375], 
        3581577: [7980255, 9434375], 7980255: [9434375], 9434375: []}

now a stack can find all possibilities

Anwser:

'''
import time, math
start_time = time.time()

def a(n):
    return [pow(153, i, 10**7 + 19) for i in range(1, n + 1)]
        
def S(n):
    A = a(n)
    res = 0
    for a1 in range(n - 4):
        A1 = A[a1]
        #print("A1", A1)
        for a2 in range(a1 + 1, n - 2):
            A2 = A[a2]
            if A2 > A1:
                #print("A2", A2)
                for a3 in range(a2 + 1, n - 1):
                    A3 = A[a3]
                    #print("A3", A3)
                    if A3 > A2:
                        for a4 in range(a3 + 1, n):
                            A4 = A[a4]
                            #print("A4", A4)
                            if A4 > A3:
                                #print(A1, A2, A3, A4)
                                res += A1 + A2 + A3 + A4
    return res
                    

if __name__ == "__main__":
    print(S(100))
    print("--- %s seconds ---" % (time.time() - start_time))
