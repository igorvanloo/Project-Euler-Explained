#Euler Problem 16
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

def sumofdigits(x):
    y = str(x)
    sumlist = list(y)
    totalsum = 0
    for i in sumlist:
        totalsum = totalsum + int(i)   
    return totalsum

