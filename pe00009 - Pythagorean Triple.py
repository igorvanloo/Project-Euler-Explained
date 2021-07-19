#Euler Problem 9
#Pythagorean Triplet a < b < c, a^2 + b^2 = c^2

def pythagoreantriplet(n,m): #This function will produce a list of all pythagorean triples
    pythtriple = []
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    pythtriple.append(a)
    pythtriple.append(b)
    pythtriple.append(c)
    return pythtriple

def pythagoreantripletsum(y): #If the sum of the pythagorean triple is 1000 it will return that triple
    requiredsum = 1000
    for i in range(y):
        for j in range(i,y):
            anwser = sum(pythagoreantriplet(i, j))
            if anwser == requiredsum:
                return (pythagoreantriplet(i, j))

def pythagoreantripletproduct(z): #Will calculate the producrt pythagorean triples where 100 > m,n
    anwser = pythagoreantripletsum(z)
    product = 1
    for i in range(0,len(anwser)):
        product = product * anwser[i]
    return product

def simplerversion(): #Much simpler version using pure brute force but 1000 is small so its okay
    requiredsum = 1000
    for a in range(1,requiredsum + 1):
        for b in range(a, requiredsum + 1):
            c = requiredsum - a - b
            if a*a + b*b == c*c:
                return a*b*c