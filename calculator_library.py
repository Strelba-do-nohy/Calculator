########################################################
# Project name: Math library for calculator
# Package: Calculator
# File: matematicka_knihovna.py
# Date: 01.04.2022
# Last changes: 27.04.2022
# Author: Strelba do nohy (Dinara Garipova -- xgarip00)
#########################################################
# @package Calculator
# @file matematicka_knihovna.py
# @author Strelba do nohy (Dinara Garipova -- xgarip00)
##########################################################

##
# @brief Checking if the user is entering numbers
# @param one is the first number
# @param two is the second number
# @return "true" if the user is entering numbers and "false" if not
def CORRECT_IN(one,two):
    if (type(one) != int and type(one) != float):
        return False
    elif (type(two) != float and type(two) != int):
        return False
    else:
        return True

##
# @brief Function PLUS requires two statements
# @param one is the first number
# @param two is the second number
# @return The sum of statements one and two
# @exception TypeError when one or two is not a number
def plus(one,two):
    if CORRECT_IN(one,two) is True:
        return round(one+two, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0
        

# @brief Function MINUS requires two statements
# @param one is the first number
# @param two is the second number
# @return The difference between of statements one and two
# @exception TypeError when one or two is not a number
def minus(one,two):
    if CORRECT_IN(one,two) is True:
        return round(one-two, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

# @brief Function UMNOZ requires two statements
# @param one is the first number
# @param two is the second number
# @return The multiplication of statements one and two
# @exception TypeError when one or two is not a number
def umnoz(one,two):
   if CORRECT_IN(one,two) is True:
        return round(one*two,7)
   else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

# @brief Function PODELI requires two statements
# @param one is the divident
# @param two is the divisor
# @return The quotient of statements one and two
# @exception TypeError when one or two is not a number
def podeli(one,two):
    if CORRECT_IN(one,two) is True:
        return round(one/two, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0


# @brief Function FAKTORIAL requirs two statements
# @param cislo is an operand that is in the factorial
# @return the factorial of cislo
# @exception TypeError when cislo not a number
# @excepption return None when cislo is not a positive number
# @excepption return 1 when cislo is 0
def faktorial(cislo):
    if CORRECT_IN(cislo,cislo) is True:
      if (cislo < 0):
         raise TypeError("Wrong input! Please write a positive number.")
      elif (cislo == 0) :
          return 1
      else:
        odpoved = 1
        for i in range(1,cislo+1):
         odpoved = odpoved * i
      return round(odpoved, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

# @brief Function EXPONENTA requirs two statements
# @param osnova is a base , 
# which is amplified
# exponenta is the **************
#The function returns the base raised to the power
def exponenta(osnova,stupen):
    if CORRECT_IN(osnova,stupen) is True:
     if (stupen == 0 or stupen < 0) and osnova == 0:
         raise TypeError("Wrong input! Please write a number stupen >0.")
     else:
         return round(osnova**stupen, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0


#Function KOREN requirs two statements
#osnova is the number from which we extract the root
#stupen is the root step
#the function returns the root of a number
def koren(osnova,stupen):
    if CORRECT_IN(osnova,stupen) is True:
        if (stupen == 0 or stupen < 0) and osnova == 0:
            raise TypeError("Wrong input! Please write a number stupen >0 and osnova !=0.")
        else:
            if osnova<0:
                if stupen%2==1:
                    osnova=osnova*(-1)
                    return -1*osnova**(1/stupen)
                else:
                    raise TypeError("Wrong input! Please write a number osnova >0.")
            return round(osnova**(1/stupen), 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0


#Function LOG requirs two statements
#osnova is the number (outline)
#cislo is the number with which I take the logarithm from the outline
#the function returns some logarifm of the number from the outline
def log(osnova,cislo):
    if CORRECT_IN(osnova,cislo) is True:
        if (osnova == 1 or osnova < 0 or cislo < 0):
            raise TypeError("Wrong input! Please write a number osnova !=1 and osnova >0 and cislo >0.")
        else:
            odpoved = (100000000.0 * ((cislo ** (1/100000000.0)) - 1)) / (100000000.0 * ((osnova ** (1/100000000.0)) - 1))
            return(round(odpoved, 7))
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0