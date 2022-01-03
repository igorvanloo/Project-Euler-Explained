'''
Project Euler Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

Anwser:
    21124
--- 0.0008409023284912109 seconds ---
'''

import time 

ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def Number_to_english(x):
    if x < 20:
        return ONES[x]
    elif 20 <= x < 100:
        return TENS[x // 10] + ONES[x % 10]
    elif 100 <= x < 1000:
        if x == 100:
            return "onehundred"
        else:
            if x % 100 == 0:
                return ONES[ x // 100] + "hundred"
            else:
                return ONES[ x // 100] + "hundred" + "and" + Number_to_english(x % 100)
    elif x == 1000:
        return "onethousand"

def sumofnumber(x):
    totalsum = sum(len(Number_to_english(i)) for i in range(1,x+1))
    return totalsum

if __name__ == "__main__":
    start_time = time.time()
    print(sumofnumber(1000))
    print("--- %s seconds ---" % (time.time() - start_time))

