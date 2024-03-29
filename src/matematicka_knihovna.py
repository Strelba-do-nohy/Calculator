"""!
* Project Name : Calculator                                               
* File : matematicka_knihovna.py                                                     
* Date : 01.04.2022                                                        
* Last change : 27.04.2022                                                 
* Author : Strelba do nohy (Dinara Garipova -- xgarip00)                                                                                                                 
* Description : Math library for calculator with basic and advanced math operations                                                                                 
"""
"""!
 @file matematicka_knihovna.py                                                        
                                                                           
 @brief Math library for calculator                                                    
 @author Strelba do nohy (Dinara Garipova -- xgarip00)
"""


def CORRECT_IN(one,two):
    """!
    @brief Checking if the user is entering numbers
    @param one is the first number
    @param two is the second number
    @return "true" if the user is entering numbers and "false" if not
    """
    if (type(one) != int and type(one) != float):
        return False
    elif (type(two) != float and type(two) != int):
        return False
    else:
        return True

def plus(one,two):
    """!
    @brief Function PLUS for addition of 2 numbers, requires two statements
    @param one is the first number
    @param two is the second number
    @return The sum of statements one and two 
    @exception TypeError when one or two is not a number
    """
    if CORRECT_IN(one,two) is True:
        return round(one+two, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0
        
def minus(one,two):
    """!
    @brief Function MINUS requires two statements
    @param one is the first number
    @param two is the second number
    @return The difference between of statements one and two
    @exception TypeError when one or two is not a number
    """
    if CORRECT_IN(one,two) is True:
        return round(one-two, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

def umnoz(one,two):
    """!
    @brief Function UMNOZ requires two statements
    @param one is the first number
    @param two is the second number
    @return The multiplication of statements one and two
    @exception TypeError when one or two is not a number
    """
    if CORRECT_IN(one,two) is True:
        return round(one*two,7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

def podeli(one,two):
    """!
    @brief Function PODELI requires two statements
    @param one is the divident
    @param two is the divisor
    @return The quotient of statements one and two
    @exception TypeError when one or two is not a number
    """
    if CORRECT_IN(one,two) is True:
        return round(one/two, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

def faktorial(cislo):
    """!
    @brief Function FAKTORIAL requirs two statements
    @param cislo is an operand that is in the factorial
    @return the factorial of cislo
    @exception TypeError when cislo not a number
    @exception TypeError when cislo is not a positive number
    @exception return 1 when cislo is 0
    """
    if CORRECT_IN(cislo,cislo) is True:
      if (cislo < 0):
         raise TypeError("Wrong input! Please write a positive number.")
      elif cislo == 0:
          return 1
      else:
        odpoved = 1
        for i in range(1,cislo+1):
         odpoved = odpoved * i
      return round(odpoved, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0


def exponenta(osnova,stupen):
    """!
    @brief Function EXPONENTA requirs two statements
    @param osnova is a base,which is amplified
    @param stupen is the exponenta
    @return The base raised osnova to the power stupen
    @exception TypeError when osnova or stupen not a number
    @exception TypeError when stupen is not a positive number
    @exception TypeError when osnova is 0
    """
    if CORRECT_IN(osnova,stupen) is True:
     if (stupen < 0) and (type(stupen) !=int):
         raise TypeError("Wrong input! Please write a natural number stupen >=0.")
     else:
         return round(osnova**stupen, 7)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

def koren(osnova,stupen):
    """!
    @brief Function KOREN requirs two statements
    @param osnova is the number from which we extract the root
    @param stupen is the root step
    @return The root of a number
    @exception TypeError when osnova or stupen not a number
    @exception TypeError when stupen is not a positive number
    @exception TypeError when osnova is 0
    """
    if CORRECT_IN(osnova,stupen) is True:
        if (stupen == 0 or stupen < 0) and (type(stupen) !=int) and osnova == 0:
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

def log(osnova,cislo):
    """!
    @brief Function LOG requirs two statements
    @param osnova is the number (outline)
    @param cislo is the number with which I take the logarithm from the outline
    @return some logarifm of the number from the outline
    @exception TypeError when osnova or cislo not a number
    @exception TypeError when cislo is not a positive number
    @exception TypeError when osnova is 1 or when osnova is not a positive number
    """
    if CORRECT_IN(osnova,cislo) is True:
        if (osnova == 1 or osnova <= 0 or cislo <= 0):
            raise TypeError("Wrong input! Please write a number osnova !=1 and osnova >0 and cislo >0.")
        else:
            odpoved = (100000000.0 * ((cislo ** (1/100000000.0)) - 1)) / (100000000.0 * ((osnova ** (1/100000000.0)) - 1))
            return(round(odpoved, 7))
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0
