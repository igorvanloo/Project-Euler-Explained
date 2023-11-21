#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:59:27 2022

@author: igorvanloo
"""
'''
Project Euler Problem 229

Just complete brute force

I could get the answer for 10^9 but 2*10^9 is causing me memory issues so compute in segments

Anwser:
    11325263
--- 1126.3620376586914 seconds ---
'''
import time, math
start_time = time.time()

def compute(limit):
        
    sqs7 = set([])
    sqs3 = set([])
    sqs2 = set([])
    sqs1 = set([])
    
    #print(7)
    for a in range(1, int(math.sqrt(limit)) + 1):
        for b in range(1, int(math.sqrt((limit - a*a)//7)) + 1):
            v = a*a + 7*b*b
            sqs7.add(v)
            
    maxsqs = max(sqs7)
    #print(3)
    for a in range(1, int(math.sqrt(maxsqs)) + 1):
        for b in range(1, int(math.sqrt((maxsqs - a*a)//3)) + 1):
            v = a*a + 3*b*b
            if v in sqs7:
                sqs3.add(v)
                
    maxsqs = max(sqs3)
    #print(2)
    for a in range(1, int(math.sqrt(maxsqs)) + 1):
        for b in range(1, int(math.sqrt((maxsqs - a*a)//2)) + 1):
            v = a*a + 2*b*b
            if v in sqs3:
                sqs2.add(v)
                
    maxsqs = max(sqs2)
    #print(1)
    for a in range(1, int(math.sqrt(maxsqs)) + 1):
        for b in range(a, int(math.sqrt((maxsqs - a*a))) + 1):
            v = a*a + b*b
            if v in sqs2:
                sqs1.add(v)
                
    return len(sqs1)

def segment(limit):
    
    segmentstart = 0
    segmentsize = limit//1000
    
    b7max = [0]*(int(math.sqrt(limit)) + 1)
    b3max = [0]*(int(math.sqrt(limit)) + 1)
    b2max = [0]*(int(math.sqrt(limit)) + 1)
    b1max = [0]*(int(math.sqrt(limit)) + 1)
    
    total = 0
    while segmentstart <= limit:
        print(segmentstart)
        segmentend = min(segmentstart + segmentsize, limit)
        
        sqs7 = set([])
        sqs3 = set([])
        sqs2 = set([])
        sqs1 = set([])
        
        #print(7)
        for a in range(1, int(math.sqrt(segmentend)) + 1):
            for b in range(b7max[a] + 1, int(math.sqrt((segmentend - a*a)//7)) + 1):
                v = a*a + 7*b*b
                sqs7.add(v)
            b7max[a] = b
                
        #print(3)
        for a in range(1, int(math.sqrt(segmentend)) + 1):
            for b in range(b3max[a] + 1, int(math.sqrt((segmentend - a*a)//3)) + 1):
                v = a*a + 3*b*b
                if v in sqs7:
                    sqs3.add(v)
            b3max[a] = b
        
        #print(2)
        for a in range(1, int(math.sqrt(segmentend)) + 1):
            for b in range(b2max[a] + 1, int(math.sqrt((segmentend - a*a)//2)) + 1):
                v = a*a + 2*b*b
                if v in sqs3:
                    sqs2.add(v)
            b2max[a] = b    
        #print(1)
        for a in range(1, int(math.sqrt(segmentend)) + 1):
            for b in range(b1max[a] + 1, int(math.sqrt((segmentend - a*a))) + 1):
                v = a*a + b*b
                if v in sqs2:
                    sqs1.add(v)
            b1max[a] = b
            
        segmentstart += segmentsize
        total += len(sqs1)
    return total

if __name__ == "__main__":
    print(segment(2*10**9))
    print("--- %s seconds ---" % (time.time() - start_time))
