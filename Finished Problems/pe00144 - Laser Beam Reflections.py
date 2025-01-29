# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:17:17 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 144

Answer:
    354
--- 0.2791154384613037 seconds ---
'''
import time, math
import matplotlib.pyplot as plt

start_time = time.time()

class Vector:
    def __init__(self, v):
        self.v = v
        self.v0 = v[0]
        self.gradient = self.v[1]/self.v[0]
    
    def __add__(self, other):
        x1, y1 = self.v
        x2, y2 = other.v
        return Vector((x1 + x2, y1 + y2))
    
    def __sub__(self, other):
        x1, y1 = self.v
        x2, y2 = other.v
        return Vector((x1 - x2, y1 - y2))
    
    def __rmul__(self, c):
        x1, y1 = self.v
        return Vector((c*x1, c*y1))
    
    def dot_prod(self, other):
        return self.v[0] * other.v[0] + self.v[1] * other.v[1]

    def norm_sq(self):
        return self.v[0]**2 + self.v[1]**2
    
    def equation(self, point):
        x2, y2 = point
        b = y2 - self.gradient * x2
        return (self.gradient, b)

def compute():
    x1, y1 = 0, 10.1
    x2, y2 = 1.4, -9.6
    
    plt.ylim(-11,11)
    plt.xlim(-6,6)
    s = [x/100 for x in range(-500, 501, 1)]
    r1 = [math.sqrt(100 - 4*i*i) for i in s]
    r2 = [-math.sqrt(100 - 4*i*i) for i in s]
    
    plt.plot(s, r1, color = "black")
    plt.plot(s, r2, color = "black")
    
    x = [x1, x2]
    y = [y1, y2]
    plt.plot(x,y)
    
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
      
    i = 1
    while True:
        #print("p1", x1, y1)
        #print("p2", x2, y2)
        #Current line vector
        m1 = (y2 - y1)/(x2 - x1) 
        V = Vector((1, m1))
        #print("Incoming", V.equation((x1, y1)))
        
        #Vector of normal of tangent line
        m2 = y2/(4*x2)
        n = Vector((1, m2))
        
        #Vector compoenent of reflecting line
        r = V - 2*V.dot_prod(n)/n.norm_sq() * n
        m3, d = r.equation((x2, y2))
        #print("Outgoing", m3, d)
        
        #4x^2 + (m3 * x + b)^2 = 100
        #(4 + m3)x^2 + 2*m3*d*x + d^2 - 100 = 0
        a, b, c = 4 + m3*m3, 2*m3*d, d*d - 100
        
        r1, r2 = (- b + math.sqrt(b*b - 4*a*c))/(2*a), (- b - math.sqrt(b*b - 4*a*c))/(2*a)
        if abs(r1 - x2) < 1/(10**8):
            r = r2
        else:
            r = r1
        x1, y1 = x2 , y2
        x2 = r
        t = math.sqrt(100 - 4*r*r)
        if abs(m3*x2 + d - t) < 1/(10**8):
            y2 = t
        else:
            y2 = -t
        
        x = [x1, x2]
        y = [y1, y2]
        plt.plot(x,y, color = "r")
    
        
        if -0.01 <= x2 <= 0.01:
            if y2 > 0:
                plt.show()
                return i

        i += 1
        
    # function to show the plot
    plt.show()

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
