#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:29:35 2021

@author: igorvanloo
"""

'''
Project Euler Problem 151

A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special colour-proofing paper of size A5.

Every Monday morning, the supervisor opens a new envelope, containing a large sheet of the special paper with size A1.

The supervisor proceeds to cut it in half, thus getting two sheets of size A2. Then one of the sheets is cut in half to get 
two sheets of size A3 and so on until an A5-size sheet is obtained, which is needed for the first batch of the week.

All the unused sheets are placed back in the envelope.


At the beginning of each subsequent batch, the supervisor takes from the envelope one sheet of paper at random. If it is of size A5, 
then it is used. If it is larger, then the 'cut-in-half' procedure is repeated until an A5-size sheet is obtained, and any remaining 
sheets are always placed back in the envelope.

Excluding the first and last batch of the week, find the expected number of times (during each week) that the supervisor finds a 
single sheet of paper in the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx .

Reasoning

I will try to build this like a game

There are 16 batches, we exclude the last and first so he has 14 "rolls" to choose from

His choices will be [(A2, 1), (A3, 1), (A4, 1), (A5,1)] on day one where A3 denotes the paper and the number next to it denotes the number of sheets left


Anwser:
    0.46476 for 10**6 options
    0.464399 is correct anwser
--- 72.09856295585632 seconds ---

    0.464399
--- 0.0014448165893554688 seconds ---
    
'''

import time, random
from collections import Counter

start_time = time.time()

def pickpaper1(paperlist, paperchoice):
    
    if paperchoice == "A2":
        paperlist.remove(paperchoice)
        paperlist.append("A3")
        paperlist.append("A4")
        paperlist.append("A5")

    elif paperchoice == "A3":
        paperlist.remove(paperchoice)
        paperlist.append("A4")
        paperlist.append("A5")
        
    elif paperchoice == "A4":
        paperlist.remove(paperchoice)
        paperlist.append("A5")
        
    elif paperchoice == "A5":
        paperlist.remove(paperchoice)

    return paperlist

def compute1(LIMIT):
    
    temp = []
    overall = []
    for x in range(LIMIT):
        
        paper = ["A2","A3","A4","A5"] #this is what he starts with on day 1
                
        for y in range(1,15):
            paperchoice = random.choice(paper)
            
            paper = pickpaper1(paper, paperchoice)
            c1 = Counter(paper)
            temp1 = []
            for x in set(paper):
                temp1.append((x, c1[x]))
            overall.append((y, str(temp1)))
            #print(action)
    final = list(set(overall))
    c = Counter(overall)
    for x in final:
        temp.append((x, c[x]/LIMIT))
    return (c[((7, "[('A2', 1)]"))]/LIMIT + c[((13, "[('A4', 1)]"))]/LIMIT + c[(11, "[('A3', 1)]")]/LIMIT)

def compute():
    possib = [(1,1,1,1)]
    prob =[1]

    stack = [(1,1,1,1)]
    
    while len(stack) != 0:        
        curr = stack.pop(0)
        length = prob[possib.index(curr)]
        
        #print(prob)
        if curr[0] != 0:
            p = curr[0]/(curr[0] + curr[1] + curr[2] + curr[3])
            new = (curr[0]-1,curr[1]+1,curr[2]+1,curr[3]+1)
            if new in possib:
                prob[possib.index(new)] += p*length
            else:
                possib.append(new)
                stack.append(new)
                prob.append(p*length)
        
        if curr[1] != 0:
            p = curr[1]/(curr[0] + curr[1] + curr[2] + curr[3])
            new = (curr[0],curr[1]-1,curr[2]+1,curr[3]+1)
            if new in possib:
                prob[possib.index(new)] += p*length
            else:
                possib.append(new)
                stack.append(new)
                prob.append(p*length)
        
        if curr[2] != 0:
            p = curr[2]/(curr[0] + curr[1] + curr[2] + curr[3])
            new = (curr[0],curr[1],curr[2]-1,curr[3]+1)
            if new in possib:
                prob[possib.index(new)] += p*length
            else:
                possib.append(new)
                stack.append(new)
                prob.append(p*length)
        
        if curr[3] != 0:
            p = curr[3]/(curr[0] + curr[1] + curr[2] + curr[3])
            new = (curr[0],curr[1],curr[2],curr[3]-1)
            if new in possib:
                prob[possib.index(new)] += p*length
            else:
                possib.append(new)
                stack.append(new)
                prob.append(p*length)
                
    return round(prob[possib.index((1,0,0,0))] + prob[possib.index((0,1,0,0))] + prob[possib.index((0,0,1,0))], 6)
            
        
    
    
    
if __name__ == "__main__":
    #print(compute1(10**5))
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))