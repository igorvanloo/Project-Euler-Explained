#Euler Problem 4

overall = []
count = 1
for x in range(100,1000):
    for y in range(100,1000):
        a = x*y
        numbers = list(str(a))
        if numbers == numbers[::-1]:
            overall.append(a)
overall = sorted(overall)
print(max(overall))

def ispalindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False
    
def main():
    overall = []
    for x in range(100,1000):
        for y in range(100,1000):
            a = x*y
            test = list(str(a))
            if ispalindrome(test) == True:
                overall.append(a)
    return max(overall)