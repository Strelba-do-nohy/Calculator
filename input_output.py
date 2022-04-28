########################################################
# Project name: Input and output for calculator
# Package: Calculator
# File: input_output.py
# Date: 06.04.2022
# Last changes: 28.04.2022
# Author: Strelba do nohy (Alina Aidusheva -- xaidus00)
#########################################################
# @package Calculator
# @file input_output.py
# @author Strelba do nohy (Alina Aidusheva -- xaidus00)
##########################################################

import matematicka_knihovna
import re

# @brief does all exponent operations in a string
# @param the current segment of the line over which calculations are performed
# @return a string with the result of the calculation inserted at the place of the operation exponent
def check_exp(result):
    for item in range(len(result)):
        search_exp = re.findall(r'\^', result[item])
        #when finding the operation
        if search_exp:
            exp = re.split(r'\^', result[item])
            #if this number is not negative
            if exp[0].isdigit():
                 x = int(exp[0])
            #if this number is negative
            elif re.match(r'/', exp[0]):
                tmp_exp = exp[0]
                exp[0] = tmp_exp[1:]
                if exp[0].isdigit():
                    x = int("-" + exp[0])
                else:
                    x = float("-" + exp[0])
            #if this number is not negative
            else:
                x = float(exp[0])
            #if this number is not negative
            if exp[1].isdigit():
                 y = int(exp[1])
            #if this number is negative
            elif re.match(r'/', exp[1]):
                tmp_exp = exp[1]
                exp[1] = tmp_exp[1:]
                if exp[1].isdigit():
                    y = int("-" + exp[1])
                else:
                    y = float("-" + exp[1])
            #if this number is not negative
            else:
                y = float(exp[1])
            result[item] = str(matematicka_knihovna.exponenta(x,y))
            if re.match(r'-', result[item]):
                tmp_exp = result[item]
                result[item] = "/" + tmp_exp[1:]
    return result

# @brief does all factorial operations in a string
# @param the current segment of the line over which calculations are performed
# @return a string with the result of the calculation inserted at the place of the operation factorial
def check_fact(result):
    for item in range(len(result)):
        search_fact = re.findall(r'\!', result[item])
        if search_fact:
            #division a number
            fact = re.split(r'\!', result[item])
            if fact[0].isdigit():
                 x = int(fact[0])
                 #insert calculations at the place of the operation without "/" (minus)
                 result[item] = str(matematicka_knihovna.faktorial(x))
            elif re.match(r'/', fact[0]):
                tmp_fact = fact[0]
                fact[0] = tmp_fact[1:]
                if fact[0].isdigit():
                    x = int(fact[0])
                    #insert calculations at the place of the operation with "/" (minus)
                    result[item] = "/" + str(matematicka_knihovna.faktorial(x))
                else:
                    x = float(fact[0])
                    #insert calculations at the place of the operation with "/" (minus)
                    result[item] = "/" + str(matematicka_knihovna.faktorial(x))
            else:
                x = float(fact[0])
                #insert calculations at the place of the operation without "/" (minus)
                result[item] = str(matematicka_knihovna.faktorial(x))
    return result

# @brief does all root operations in a string
# @param the current segment of the line over which calculations are performed
# @return a string with the result of the calculation inserted at the place of the operation root  
def check_kor(result):
    for item in range(len(result)):
        search_kor = re.findall(r'√', result[item])
        #when finding the operation root
        if search_kor:
            kor = re.split(r'√', result[item])
            #flag_min is a flag indicating sign before number
            flag_min = 0
            if re.match(r'/', kor[0]):
                flag_min = 1
                tmp_kor = kor[0]
                kor[0] = tmp_kor[1:]
            if kor[0]:
                if kor[0].isdigit():
                    x = int(kor[0])
                else:
                    x = float(kor[0])
            else:
                x = int(2)
            
            if kor[1].isdigit():
                 y = int(kor[1])
            elif re.match(r'/', kor[1]):
                tmp_kor = kor[1]
                kor[1] = tmp_kor[1:]
                if kor[1].isdigit():
                    y = int("-" + kor[1])
                else:
                    y = float("-" + kor[1])
            else:
                y = float(kor[1])
            #insert calculations at the place of the operation with/without "/" (minus)
            if flag_min:
                result[item] = "/" + str(matematicka_knihovna.koren(y, x))
            else:
                result[item] = str(matematicka_knihovna.koren(y, x))
            if re.match(r'-', result[item]):
                result[item] = "/" + result[item][1:]
            if re.match(r'/-', result[item]):
                result[item] = result[item][2:]
    return result

# @brief does all logarithm operations in a string
# @param the current segment of the line over which calculations are performed
# @return a string with the result of the calculation inserted at the place of the operation logarigm   
def check_log(result):
    for item in range(len(result)):
        search_log = re.findall(r'log', result[item])
        #when finding the operation logarithm
        if search_log:
            loga = result[item]
            #deleting elements "log"
            result[item] = loga[3:]
            #division into base and number
            loga = re.split(r'\|', result[item])
            #if this number is negative
            if re.match(r'/', loga[0]):
                loga[0]=loga[0][1:]
                if loga[0].isdigit():
                    x = int("-" + loga[0])
                else:
                    x = float("-" + loga[0])
            #if this number is not negative
            else:
                if loga[0].isdigit():
                    x = int(loga[0])
                else:
                    x = float(loga[0])
            print(x)
            #if this number is negative
            if re.match(r'/', loga[1]):
                loga[1]=loga[1][1:]
                if loga[1].isdigit():
                    y = int("-" + loga[1])
                else:
                    y = float("-" + loga[1])
            #if this number is not negative
            else:
                if loga[1].isdigit():
                    y = int(loga[1])
                else:
                    y = float(loga[1])
            #insert calculations at the place of the operation plus
            result[item] = str(matematicka_knihovna.log(x,y))
            #replace "-" with a character "/"
            if re.match(r'-', result[item]):
                result[item] = "/" + result[item][1:]
    return result

# @brief does all multiplication operations in a string
# @param the current segment of the line over which calculations are performed
# @return a string with the result of the calculation inserted at the place of the operation multiplication
def check_mul(result):
    #concatenation of elements in a string
    result = " ".join(result)
    #count_min is a number of the "*"
    count_mul = re.findall(r'\*', result)
    count_mul = len(count_mul)
    result = parse(result)
    while count_mul>0:
        for item in range(len(result)):
            #when finding the operation
            if result[item]=="*":
                #flag_min_x is a flag indicating sign before x
                #flag_min_y is a flag indicating sign before y
                flag_min_x=0
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                #if this number is simple
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                #if this number is not simple (have a ".")
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                #if this number is simple
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                #if this number is not simple (have a ".")
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.umnoz(x,y))
                #replace "-" with a character "/"
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_mul-=1
                #insert calculations at the place of the operation
                result = result[:item-1] + result[item+1:]
                break
    return result

# @brief does all division operations in a string
# @param the current segment of the line over which calculations are performed
# @return a string with the result of the calculation inserted at the place of the operation division
def check_div(result):
    #concatenation of elements in a string
    result = " ".join(result)
    #count_min is a number of the "÷"
    count_div = re.findall(r'÷', result)
    count_div = len(count_div)
    result = parse(result)
    while count_div>0:
        for item in range(len(result)):
            #when finding the operation division
            if result[item]=="÷":
                #flag_min_x is a flag indicating sign before x
                #flag_min_y is a flag indicating sign before y
                flag_min_x=0
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                #if this number is simple
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                #if this number is not simple (have a ".")
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                #if this number is simple
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                #if this number is not simple (have a ".")
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.podeli(x,y))
                #replace "-" with a character "/"
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_div-=1
                #insert calculations at the place of the operation
                result = result[:item-1] + result[item+1:]
                break
    return result

# @brief does all plus operations in a string
# @param the current segment of the line over which calculations are performed
# @return a string with the result of the calculation inserted at the place of the operation plus
def check_plus(result):
    #concatenation of elements in a string
    result = " ".join(result)
    #count_min is a number of the "+"
    count_plus = re.findall(r'\+', result)
    count_plus = len(count_plus)
    result = parse(result)
    while count_plus>0:
        for item in range(len(result)):
            #when finding the operation plus
            if result[item]=="+":
                #flag_min_x is a flag indicating sign before x
                flag_min_x=0
                #flag_min_y is a flag indicating sign before y
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                #if this number is simple
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                #if this number is not simple (have a ".")
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                #if this number is simple
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                #if this number is not simple (have a ".")
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.plus(x,y))
                #replace "-" with a character "/"
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_plus-=1
                #insert calculations at the place of the operation plus
                result = result[:item-1] + result[item+1:]
                break
    return result

# @brief does all minus operations in a string
# @param the current segment of the line over which calculations are performed
# @return a string with the result of the calculation inserted at the place of the operation minus
def check_minus(result):
    #concatenation of elements in a string
    result = " ".join(result)
    #count_min is a number of the "-"
    count_min = re.findall(r'-', result)
    count_min = len(count_min)
    result = parse(result)
    while count_min>0:
        for item in range(len(result)):
            #when finding the operation minus
            if result[item]=="-":
                #flag_min_x is a flag indicating sign before x
                flag_min_x=0
                #flag_min_y is a flag indicating sign before y
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                #if this number is simple
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                #if this number is not simple (have a ".")
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                #if this number is simple
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                #if this number is not simple (have a ".")
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.minus(x,y))
                #replace "-" with a character "/"
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_min-=1
                #insert calculations at the place of the operation minus
                result = result[:item-1] + result[item+1:]
                break
    return result

# @brief does the calculations specified in the line in the correct order
# @param the current segment of the line over which calculations are performed
# @return a string containing the result of all calculations on the current string segment
def math_work (line):
    result = parse(line)
    result = check_exp(result)
    result = check_fact(result)
    result = check_kor(result)
    result = check_log(result)
    result = check_mul(result)
    result = check_div(result)
    result = check_plus(result)
    result = check_minus(result)
    #concatenation of elements in a string
    result = " ".join(result)
    return result

# @brief Dividing a string into groups of characters necessary for the correct operation of computational functions
# @param line is the string we received from the function "math_work"
# @return a parsed string for the correct operation of computational functions
def parse(line):
    #change is a list of all logarithms in a line
    change = re.findall(r'log[0-9]+|log /[0-9]+', line) + re.findall(r'log/[0-9]+', line)
    #in the logarithm, we separate the base from the number with a sign "|"
    for item in change:
        line = re.sub(item, item+"|", line)
    #split a string into separate characters
    line = list(line)
    #result is a new line where we will write the results of various calculations
    result = ""
    #grouping characters for the correct work of functions
    for character in line:
        #a space is not written to the result string
        if character==" ":
            continue
        #numbers and special characters go without spaces
        if character.isdigit():
            result+=str(character)
        elif character=="." or character=="^" or character=="!" or character=="√" or character=="l" or character=="o" or character=="g" or character=="|" or character=="/":
            result+=str(character)
        else:
            #in case it is a character not listed as special above, it is written to the string between spaces
            result+=" "+ str(character) + " "
    #removing double spaces
    while "  " in result:
        result= result.replace("  ", " ")
    #if the first character is a minus, replace it with a character "/"
    if re.match(r' -', result):
        result = "/" + result[3:]
    #delete two characters "//"
    if re.match(r'//', result):
        result = result[2:]
    #split string by spaces
    result = result.split()
    return result

# @brief Function "check_brackets" checking if the user is entering the correct number of brackets and controling their position
# @param line is the original string we received from the user
# @return "0" if the user is entering brackets correctly and "1" if not
def check_brackets (line):
    #count is a number of the opening brackets
    count=0
    for sign in line:
        if sign == "(":
            count+=1
        if sign == ")":
            count-=1
            if count<0:
                return 1
    if count==0: return 0
    else: return 1

# @brief Calculations in brackets and returning a string with a result of calculations
# @param br is a number of the opening brackets "("
# @param calculation is a string containing all calculations
# @return a string containing the final result of all calculations, including all calculations in brackets
def brackets(calculation, br):
    #left is the index of the position in the line of the last "(" found at the current time
    left=0
    #right is the index of the position in the line of the first ")" found at the current time
    right=0
    #while there are still brackets in the string
    while br>0:
        #find "left" and "right"
        for item in range(len(calculation)):
             if calculation[item]==")":
                right=item
                break
        for item in range(len(calculation[:right])):
             if calculation[item]=="(":
                left=item
        #tmp_line is a part of the string contained in brackets, which is sent in the function "math_work" for further calculations
        tmp_line=calculation[left+1:right]
        #insert the result of the calculations in the "tmp_line" in string
        calculation = calculation[:left] + " " + str(math_work(tmp_line)) + " " + calculation[right+1:]
        br-=1
    return calculation
######################################################################################################################################
#End of file input_output.py
#######################################################################################################################################