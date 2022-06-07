"""!
* Project Name : Calculator                                               
* File : input_output.py                                                     
* Date : 06.04.2022                                                        
* Last change : 28.04.2022                                                 
* Author : Strelba do nohy (Alina Aidusheva -- xaidus00)                                                                                                                 
* Description : Input and output for calculator, parsing and working with a string                                                                                 
"""
"""!
 @file input_output.py                                                                     
 @brief Input and output for calculator                                                   
 @author Strelba do nohy (Alina Aidusheva -- xaidus00)
"""

import matematicka_knihovna
import re

def check_exp(result):
    """!
    @brief does all exponent operations in a string
    @param result the current segment of the line over which calculations are performed
    @return a string with the result of the calculation inserted at the place of the operation exponent
    """
    #all actions are similar to the functions check_log, check_kor and check_fact
    for item in range(len(result)):
        search_exp = re.findall(r'\^', result[item])
        if search_exp:
            exp = re.split(r'\^', result[item])
            if exp[0].isdigit():
                 x = int(exp[0])
            elif re.match(r'/', exp[0]):
                tmp_exp = exp[0]
                exp[0] = tmp_exp[1:]
                if exp[0].isdigit():
                    x = int("-" + exp[0])
                else:
                    x = float("-" + exp[0])
            else:
                x = float(exp[0])
            if exp[1].isdigit():
                 y = int(exp[1])
            elif re.match(r'/', exp[1]):
                tmp_exp = exp[1]
                exp[1] = tmp_exp[1:]
                if exp[1].isdigit():
                    y = int("-" + exp[1])
                else:
                    y = float("-" + exp[1])
            else:
                y = float(exp[1])
            result[item] = str(matematicka_knihovna.exponenta(x,y))
            if re.match(r'-', result[item]):
                tmp_exp = result[item]
                result[item] = "/" + tmp_exp[1:]
    return result

def check_fact(result):
    """!
    @brief does all factorial operations in a string
    @param result the current segment of the line over which calculations are performed
    @return a string with the result of the calculation inserted at the place of the operation factorial
    """
    for item in range(len(result)):
        search_fact = re.findall(r'\!', result[item]) #searched in string factorial
        if search_fact: #if the factorial is found
            fact = re.split(r'\!', result[item]) #separates the sign "!"
            if fact[0].isdigit(): #if x is int
                 x = int(fact[0])
                 result[item] = str(matematicka_knihovna.faktorial(x))
            elif re.match(r'/', fact[0]): #if before x stands "-"
                tmp_fact = fact[0]
                fact[0] = tmp_fact[1:]
                if fact[0].isdigit():
                    x = int(fact[0])
                    result[item] = "/" + str(matematicka_knihovna.faktorial(x))
                else:
                    x = float(fact[0])
                    result[item] = "/" + str(matematicka_knihovna.faktorial(x))
            else: #if x is float
                x = float(fact[0])
                result[item] = str(matematicka_knihovna.faktorial(x))
    return result

def check_kor(result):
    """!
    @brief does all root operations in a string
    @param result the current segment of the line over which calculations are performed
    @return a string with the result of the calculation inserted at the place of the operation root  
    """
    #all actions are similar to the functions check_kor
    for item in range(len(result)):
        search_kor = re.findall(r'√', result[item])
        if search_kor:
            kor = re.split(r'√', result[item])
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
            if flag_min:
                result[item] = "/" + str(matematicka_knihovna.koren(y, x))
            else:
                result[item] = str(matematicka_knihovna.koren(y, x))
            if re.match(r'-', result[item]):
                result[item] = "/" + result[item][1:]
            if re.match(r'/-', result[item]):
                result[item] = result[item][2:]
    return result

def check_log(result):
    """!
    @brief does all logarigm operations in a string
    @param result the current segment of the line over which calculations are performed
    @return a string with the result of the calculation inserted at the place of the operation logarigm   
    """
    for item in range(len(result)):
        search_log = re.findall(r'log', result[item]) #find all log constructions in the string
        if search_log:
            loga = result[item]
            result[item] = loga[3:] #cut characters "log"
            loga = re.split(r'\|', result[item]) #separates "\"
            if re.match(r'/', loga[0]): #if find '/', add minus sign to number
                loga[0]=loga[0][1:] 
                if loga[0].isdigit():
                    x = int("-" + loga[0]) #if x is int
                else:
                    x = float("-" + loga[0]) #if x is float
            else: #if number is positive
                if loga[0].isdigit():
                    x = int(loga[0]) #if x is int
                else:
                    x = float(loga[0]) #if x is float
            if re.match(r'/', loga[1]):  #if find '/', add minus sign to number
                loga[1]=loga[1][1:]
                if loga[1].isdigit():
                    y = int("-" + loga[1]) #if x is int
                else:
                    y = float("-" + loga[1]) #if x is float
            else: #if number is positive
                if loga[1].isdigit():
                    y = int(loga[1]) #if x is int
                else:
                    y = float(loga[1]) #if x is float
            result[item] = str(matematicka_knihovna.log(x,y)) #sends values x and y to the log function, get the answer in result[item]
            if re.match(r'-', result[item]):
                result[item] = "/" + result[item][1:] #replacing the minus with "/"
    return result


def check_div(result):
    """!
    @brief does all division operations in a string
    @param result the current segment of the line over which calculations are performed
    @return a string with the result of the calculation inserted at the place of the operation division
    """
    result = " ".join(result)
    count_div = re.findall(r'÷', result)
    count_div = len(count_div) #number of character "÷" in the string
    result = parse(result)
    while count_div>0: #as long as there are "÷" in the line
        for item in range(len(result)):
            if result[item]=="÷":
                flag_min_x=0 # "1" if x is a negative number, else "0"
                flag_min_y=0 # "1" if y is a negative number, else "0"
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                if result[item-1].isdigit(): #if x is int
                    if flag_min_x:
                        x = int("-" + result[item-1]) #add minus sign to number if flag is 1
                    else:
                        x = int(result[item-1])
                else: #if x is float
                    if flag_min_x:
                        x = float("-" + result[item-1]) #add minus sign to number if flag is 1
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                if result[item+1].isdigit(): #if y is int
                    if flag_min_y:
                        y = int("-" + result[item+1]) #add minus sign to number if flag is 1
                    else:
                        y = int(result[item+1])
                else: #if x is float
                    if flag_min_y:
                        y = float("-" + result[item+1]) #add minus sign to number if flag is 1
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.podeli(x,y)) #sends values x and y to the "podeli" function, get the answer in result[item+1]
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:] #replacing the minus with "/"
                count_div-=1 #the number of remaining actions with a "÷" in the line decreased by one
                result = result[:item-1] + result[item+1:] #cutting the string
                break
    return result

def check_mul(result):
    """!
    @brief does all multiplication operations in a string
    @param result the current segment of the line over which calculations are performed
    @return a string with the result of the calculation inserted at the place of the operation multiplication
    """
    #all actions are similar to the functions check_div, check_min, check_plus
    result = " ".join(result)
    count_mul = re.findall(r'\*', result)
    count_mul = len(count_mul)
    result = parse(result)
    while count_mul>0:
        for item in range(len(result)):
            if result[item]=="*":
                flag_min_x=0
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.umnoz(x,y))
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_mul-=1
                result = result[:item-1] + result[item+1:]
                break
    return result

def check_plus(result):
    """!
    @brief does all plus operations in a string
    @param result the current segment of the line over which calculations are performed
    @return a string with the result of the calculation inserted at the place of the operation plus
    """
    result = " ".join(result)
    count_plus = re.findall(r'\+', result)
    count_plus = len(count_plus) #number of character "+" in the string
    result = parse(result)
    while count_plus>0: #as long as there are pluses in the line
        for item in range(len(result)):
            if result[item]=="+":
                flag_min_x=0 # "1" if x is a negative number, else "0"
                flag_min_y=0 # "1" if y is a negative number, else "0"
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                if result[item-1].isdigit(): #if x is int
                    if flag_min_x:
                        x = int("-" + result[item-1]) #add minus sign to number if flag is 1 
                    else:
                        x = int(result[item-1])
                else: #if x is float
                    if flag_min_x:
                        x = float("-" + result[item-1]) #add minus sign to number if flag is 1
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                if result[item+1].isdigit(): #if x is int
                    if flag_min_y:
                        y = int("-" + result[item+1]) #add minus sign to number if flag is 1 
                    else:
                        y = int(result[item+1])
                else: #if y is float
                    if flag_min_y:
                        y = float("-" + result[item+1]) #add minus sign to number if flag is 1 
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.plus(x,y)) #sends values x and y to the plus function, get the answer in result[item+1]
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:] #replacing the minus with "/"
                count_plus-=1 #the number of remaining actions with a plus in the line decreased by one
                result = result[:item-1] + result[item+1:] #cutting the string to the value (before: a-x+y, after: a-c)
                break
    return result

def check_minus(result):
    """!
    @brief Does all minus operations in a string
    @param result the current segment of the line over which calculations are performed
    @return a string with the result of the calculation inserted at the place of the operation minus
    """
    result = " ".join(result)
    count_min = re.findall(r'-', result)
    count_min = len(count_min) #number of character "-" in the string
    result = parse(result)
    while count_min>0: #as long as there are minuses in the line
        for item in range(len(result)):
            if result[item]=="-":
                flag_min_x=0 # "1" if x is a negative number, else "0"
                flag_min_y=0 # "1" if y is a negative number, else "0"
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                if result[item-1].isdigit(): #if x is int
                    if flag_min_x:
                        x = int("-" + result[item-1]) #add minus sign to number if flag is 1
                    else:
                        x = int(result[item-1])
                else: #if x is float
                    if flag_min_x:
                        x = float("-" + result[item-1]) #add minus sign to number if flag is 1
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                if result[item+1].isdigit(): #if y is int
                    if flag_min_y:
                        y = int("-" + result[item+1]) #add minus sign to number if flag is 1
                    else:
                        y = int(result[item+1])
                else: #if y is float
                    if flag_min_y:
                        y = float("-" + result[item+1]) #add minus sign to number if flag is 1
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.minus(x,y)) #sends values x and y to the minus function, get the answer in result[item+1]
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:] #replacing the minus with "/"
                count_min-=1 #the number of remaining actions with a minus in the line decreased by one
                result = result[:item-1] + result[item+1:] #cutting the string to the value (before: a+x-y, after: a+c)
                break
    return result

def math_work (line):
    """!
    @brief Does the calculations specified in the line in the correct order
    @param line the current segment of the line over which calculations are performed
    @return a string containing the result of all calculations on the current string segment
    """
    result = parse(line)
    result = check_exp(result)
    result = check_fact(result)
    result = check_kor(result)
    result = check_log(result)
    result = check_mul(result)
    result = check_div(result)
    result = check_plus(result)
    result = check_minus(result)
    result = " ".join(result)
    return result


def parse(line):
    """!
    @brief Dividing a string into groups of characters necessary for the correct operation of computational functions
    @param line is the string we received from the function "math_work"
    @return a parsed string for the correct operation of computational functions
    """
    change = re.findall(r'log[0-9]+|log /[0-9]+', line) + re.findall(r'log/[0-9]+', line) #find all log constructs
    for item in change:
        line = re.sub(item, item+"|", line) #attaches "|" to all log constructions
    line = list(line) #built-in mutable sequence.
    result = ""
    for character in line: #all characters are entered into the new line "result", those that are not specified in the elsif are written with spaces
        if character==" ":
            continue
        if character.isdigit():
            result+=str(character)
        
        elif character=="." or character=="^" or character=="!" or character=="√" or character=="l" or character=="o" or character=="g" or character=="|" or character=="/":
            result+=str(character)
        else:
            result+=" "+ str(character) + " "
    while "  " in result:
        result= result.replace("  ", " ") #remove extra spaces
    if re.match(r' -', result):
        result = "/" + result[3:] #replacing the minus in front of the line with "/"
    if re.match(r'//', result):
        result = result[2:] #and removing the double "/" (since it's equivalent to -(-x) )
    result = result.split()
    return result

def check_brackets (line):
    """!
    @brief Function "check_brackets" checking if the user is entering the correct number of brackets and controling their position
    @param line is the original string we received from the user
    @return "0" if the user is entering brackets correctly and "1" if not
    """
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

def brackets(calculation, br):
    """!
    @brief Calculations in brackets and returning a string with a result of calculations
    @param br is a number of the opening brackets "("
    @param calculation is a string containing all calculations
    @return a string containing the final result of all calculations, including all calculations in brackets
    """
    left=0
    right=0
    while br>0:
        for item in range(len(calculation)):
             if calculation[item]==")":
                right=item
                break
        for item in range(len(calculation[:right])):
             if calculation[item]=="(":
                left=item
        tmp_line=calculation[left+1:right]
        calculation = calculation[:left] + " " + str(math_work(tmp_line)) + " " + calculation[right+1:]
        br-=1
    return calculation
