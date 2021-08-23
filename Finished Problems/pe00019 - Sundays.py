'''
Project Euler Problem 19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Anwser:
    171
--- 0.00042176246643066406 seconds ---
'''

import time, datetime #Special module in python

def cheatingway():
    count = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if datetime.date(y, m, 1).weekday() == 6:
                count += 1
    return count

if __name__ == "__main__":
    start_time = time.time()
    print(cheatingway())
    print("--- %s seconds ---" % (time.time() - start_time))
