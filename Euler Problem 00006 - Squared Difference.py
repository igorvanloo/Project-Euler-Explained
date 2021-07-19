#Euler problem 6
#FInd the difference between the square of the sum and the indivdual numbers squared

def individualsquaredsum(y):
    totalsum = 0
    for i in range(1,y):
        totalsum = totalsum + i**2
    return int(totalsum)
    

def totalsquaredsum(y):
    totalsum1 = int((sum(x for x in range(1,y))))**2
    return int(totalsum1)
    

def difference(y):
    return totalsquaredsum(y) - individualsquaredsum(y)
    
print(difference(101))
