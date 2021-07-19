#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 00:56:36 2021

@author: igorvanloo
"""

'''
Project Euler Problem 607

Marsh crossing

Reasoning

Using Snells law with a varying starting angle we can calculate the distance and find the minimum travel path

Anwser:
    [13.1265108586, [[0.9998205886512117, 19.1604708473], [0.8590717806, 15.310638357], [0.7383915199, 13.5216963021], [0.6297736235, 12.3737742605], [0.5291785536, 11.5845048492], [0.4342024767, 11.0228567497], 19.1606550106]]
--- 17.728596210479736 seconds ---
'''

import time, math
import matplotlib.pyplot as plt

start_time = time.time()

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
def compute():
    s = round((100/math.sqrt(2) - 50)/2, 10) #This is how far the marsh is
    temp = []
    for x in range(1,900001):
        theta1 = (x/10000) * math.pi/180 #Allows for smaller angle computation
        d1 = round(s/math.cos(theta1), 10) #First distance travel
        h1 = round(s*math.tan(theta1), 10) #First height achieved
        
        theta2 = round(math.asin((9*math.sin(theta1))/10), 10)
        d2 = round(10/math.cos(theta2), 10)
        h2 = round(10*math.tan(theta2), 10)
        
        theta3 = round(math.asin((8*math.sin(theta2))/9) , 10)
        d3 = round(10/math.cos(theta3), 10)
        h3 = round(10*math.tan(theta3), 10)
        
        theta4 = round(math.asin((7*math.sin(theta3))/8), 10)
        d4 = round(10/math.cos(theta4), 10)
        h4 = round(10*math.tan(theta4), 10)
        
        theta5 = round(math.asin((6*math.sin(theta4))/7), 10) 
        d5 = round(10/math.cos(theta5), 10)
        h5 = round(10*math.tan(theta5), 10)
        
        theta6 = round(math.asin((5*math.sin(theta5))/6) , 10)
        d6 = round(10/math.cos(theta6), 10)
        h6 = round(10*math.tan(theta6), 10)
        
        d7 = round(distance((50+s, h2+h3+h4+h5+h6+h1),(100/math.sqrt(2),100/math.sqrt(2))), 10)
        
        overalldistance = round(d1/10 + d2/9 + d3/8 + d4/7 + d5/6 + d6/5 + d7/10, 10)
        temp.append([overalldistance, [[theta1,d1],[theta2,d2],[theta3,d3],[theta4,d4],[theta5,d5],[theta6,d6],d7],[h1,h1+h2,h1+h2+h3,h1+h2+h3+h4,h1+h2+h3+h4+h5,h1+h2+h3+h4+h5+h6]])
    return min(temp)           

s = round((100/math.sqrt(2) - 50)/2, 10)
h = 100/math.sqrt(2)
plt.ylim(0,h)
plt.xlim(0,h)

x = [0,s, s+10, s+20, s+30, s+40, s+50, h]
y = [0,s, s+10, s+20, s+30, s+40, s+50, h]
plt.plot(x,y)
x1 = [s,s]
y1 = [0,h]
plt.plot(x1,y1, color='black', linestyle='dashed')
x2 = [s+10,s+10]
y2 = [0,h]
plt.plot(x2,y2, color='black', linestyle='dashed')
x3 = [s+20,s+20]
y3 = [0,h]
plt.plot(x3,y3, color='black', linestyle='dashed')
x4 = [s+30, s+30]
y4 = [0,h]
plt.plot(x4,y4, color='black', linestyle='dashed')
x5 = [s+40, s+40]
y5 = [0,h]
plt.plot(x5,y5, color='black', linestyle='dashed')
x6 = [s+50, s+50]
y6 = [0,h]
plt.plot(x6,y6, color='black', linestyle='dashed')

temp = [13.1265108586, [[0.9998205886512117, 19.1604708473], [0.8590717806, 15.310638357], [0.7383915199, 13.5216963021], [0.6297736235, 12.3737742605], [0.5291785536, 11.5845048492], [0.4342024767, 11.0228567497], 19.1606550106], [16.1211226673, 27.7148988812, 36.816342222, 44.104022885300004, 49.952163838000004, 54.5893365677]]
plt.title("Frodo and Sam's Path")
values = temp[2]

x7 = [0,s, s+10, s+20, s+30, s+40, s+50, h]
y7 = [0,values[0], values[1], values[2], values[3], values[4], values[5], h]

plt.plot(x7,y7, color='red')

plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# function to show the plot
plt.show()

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))