# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:21:55 2022

@author: igorvanloo
"""
'''
Project Euler Problem 504

Let ABCD be a quadrilateral whose vertices are lattice points lying on the coordinate axes as follows:

A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a, b, c, d ≤ m and a, b, c, d, m are integers.

It can be shown that for m = 4 there are exactly 256 valid ways to construct ABCD. Of these 256 quadrilaterals, 42 of them strictly contain a square number of lattice points.

How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?

Picks Theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem

A = i + b/2 - 1, A = Area of Quad, i = #of interior points, b = Number of integer boundary points

We have a Quad A(a, 0), B(0, b), C(−c, 0), D(0, −d)

Therefore the Area of this quad is the sum of 4 triangles, 
Area of top right quadrant = 1/2(a*b)
Area of top left quadrant = 1/2(b*c)
Area of bottom right quadrant = 1/2(a*d)
Area of bottom left quadrant = 1/2(c*d)

Therefore Area of Quad = 1/2(ab + bc + ad + cd) = 1/2(a(b + d) + c(b + d)) = 1/2(a + c)(b + d)

I noticed from playing around on desmos, that the he segment between A and B has 
g = gcd(a, b) + 1 integer boundary points, including themselves. Why is this?

Suppose g = gcd(a, b), the line segment between A, B can be parameterized as y = mx + c
0 = ma + c
b = c => 0 = ma + b => m = -b/a therefore the line is y = (-b/a)x + b, 0 <= x <= a

Now it is clear why, (-b/a)x must be an integer, and x is an integer, therefore if gcd(a, b) = 1, then the only x
in the allowed range is 0 and a

if g = gcd(a, b) > 1, then b/a = gb_1/ga_1 = b_1/a_1 therefore x has to be a multiple of a_1 there will be g + 2 of them

Now we know the area and #boundary points and we have i = A - b/2 + 1 

Anwser:
    694687
--- 102.26374864578247 seconds ---
'''
import time, math
start_time = time.time()

def is_quadratic(x):
    sqrt_root = (x ** (1 / 2))
    if round(sqrt_root) ** 2 == x:
        return True
    return False

def gcd(m):
    array = [[1]*(m + 1) for _ in range(m + 1)]
    for i in range(2, m + 1):
        for j in range(i, m + 1):
            array[i][j] = math.gcd(i, j)
            array[j][i] = array[i][j]
    return array
    
def compute(m):
    valid = 0
    g = gcd(m)
    for a in range(1, m + 1):
        for b in range(1, m + 1):
            for c in range(1, m + 1):
                for d in range(1, m + 1):
                    boundary_points = g[a][b] + g[b][c] + g[a][d] + g[c][d]
                    A = (a + c)*(b + d)/2
                    i = A - boundary_points/2 + 1
                    if is_quadratic(i):
                        valid += 1
    return valid
                    
if __name__ == "__main__":
    print(compute(100))
    print("--- %s seconds ---" % (time.time() - start_time))
