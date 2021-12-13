#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:38:12 2021

@author: igorvanloo
"""

'''
Project Euler Problem 610

{I, V, X, L, C, D, M, #}

After writing a monte carlo simulation and running 200,000 numbers I get an estimate of about 318-319

Let X denote the roman numeral I obtain after randomaly selecting digits then

P{X = i} = ?

Anwser:

'''

import time, math, random
start_time = time.time()

def random_generator():
    num = [x for x in range(1,101)]
    choice = random.choice(num)
    if choice <= 2:
        return "#"
    else:
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        return random.choice(roman)
    
def number_to_roman_numeral(x):
    number_of_m = int(x / 1000)
    number_of_D = int((x - number_of_m*1000) / 500)
    number_of_c = int((x - number_of_m*1000 - number_of_D*500) / 100)
    number_of_L = int((x - number_of_m*1000 - number_of_D*500 - number_of_c*100) / 50)
    number_of_x = int((x - number_of_m*1000 - number_of_D*500 - number_of_c*100 - number_of_L*50) / 10)
    number_of_I = int(x - number_of_m*1000 - number_of_D*500 - number_of_c*100 - number_of_L*50 - number_of_x*10)
    
    new_x = ""
    
    if number_of_m > 0:
        new_x += "M"*number_of_m
        
    if number_of_D > 0 or number_of_c > 0:
        if number_of_D > 0:
            if number_of_c == 4:
                new_x += "CM"
            else:
                new_x += "D"
                new_x += "C"*number_of_c
        else:
            if number_of_c == 4:
                new_x += "CD"
            else:
                new_x += "C"*number_of_c
    
    if number_of_L > 0 or number_of_x > 0:
        if number_of_L > 0:
            if number_of_x == 4:
                new_x += "XC"
            else:
                new_x += "L"
                new_x += "X"*number_of_x
        else:
            if number_of_x == 4:
                new_x += "XL"
            else:
                new_x += "X"*number_of_x
            
    if number_of_I > 0:
        if number_of_I < 4:
            new_x += "I"*number_of_I
        elif number_of_I == 4:
            new_x += "IV"
        elif number_of_I == 5:
            new_x += "V"
        elif number_of_I == 9:
            new_x += "IX"
        else:
            new_x += "V"
            new_x += "I"*(number_of_I-5)

    return new_x

def roman_numeral_to_number(x):
    temp_list = list(x)
    temp_list.append("end")
    total = 0
    for i in range(len(temp_list)):
        if temp_list[i] == "M":
            total += 1000
            
        if temp_list[i] == "D":
            total += 500
            
        if temp_list[i] == "C":
            if temp_list[i+1] == "M":
                total -= 100
            elif temp_list[i+1] == "D":
                total -= 100
            elif temp_list[i+1] == "end":
                total += 100
                break
            else:
                total += 100
                
        if temp_list[i] == "L":
            total += 50
            
        if temp_list[i] == "X":
            if temp_list[i+1] == "C":
                total -= 10
            elif temp_list[i+1] == "L":
                total -= 10
            elif temp_list[i+1] == "end":
                total += 10
                break
            else:
                total += 10
        
        if temp_list[i] == "V":
            total += 5
        
        if temp_list[i] == "I":
            if temp_list[i+1] == "X":
                total -= 1
            elif temp_list[i+1] == "V":
                total -= 1
            elif temp_list[i+1] == "end":
                total += 1
                break
            else:
                total += 1
        
        elif temp_list[i] == "end":
            break
        
    return total

def monte_carlo(trials):
    total = 0
    for x in range(trials):
        rom_num = ""
        while True:
            curr = random_generator()
            if curr == "#":
                break
            else:
                temp = rom_num + curr
                if number_to_roman_numeral(roman_numeral_to_number(temp)) == temp:
                    rom_num = temp
        if rom_num != "":
            x = roman_numeral_to_number(rom_num)
            total += x
    return total/trials
    
if __name__ == "__main__":
    print(monte_carlo(200000))
    print("--- %s seconds ---" % (time.time() - start_time))