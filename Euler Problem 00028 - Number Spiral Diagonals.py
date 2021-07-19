#Project Euler Problem 28
'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 
spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def sumofcorners(x):
    if x == 1:
        return 1
    elif x % 2 == 0:
        return "Please put odd integer"
    else:
        d = x - 1
        top_right_corner = x*x
        top_left_corner = top_right_corner - d
        bottom_left_corner = top_right_corner - 2*d
        bottom_right_corner = top_right_corner - 3*d
        #We could also compute sum of ring is 4x^2-6(x-1)
        return top_right_corner + top_left_corner + bottom_left_corner + bottom_right_corner
    
def sumofallcorners(x):
    totalsum = 0
    for i in range(1,x+1,2):
        totalsum = totalsum + sumofcorners(i)
    return totalsum
            
print(sumofallcorners(1001))