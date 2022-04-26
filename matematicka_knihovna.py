#IVS_project_2_kalkulacka
#matematicka knihovna
#strelba_do_nohy
#Dinara_Garipova xgarip00
#Datum 01.04.2022

#The function CORRECT_IN cheks, 
# if the user specifies numbers, 
#if not then does not count anything
def CORRECT_IN(one,two):
    if (type(one) != int and type(one) != float):
        return False
    elif (type(two) != float and type(two) != int):
        return False
    else:
        return True

#Function PLUS requires two statements
#one is the first statement
#two is the second statement
#the function reterns sum of statements one and two
def plus(one,two):
    if CORRECT_IN(one,two) is True:
        return round(one+two, 8)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0
        

#Function MINUS requires two statements
#one is the first statement
#two is the second statement
#the function reterns difference between of statements one and two
def minus(one,two):
    if CORRECT_IN(one,two) is True:
        return round(one-two, 8)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

#Function UMNOZ requires two statements
#one is the first statement
#two is the second statement
#the function reterns multiplication of statements one and two
def umnoz(one,two):
   if CORRECT_IN(one,two) is True:
        return round(one*two,8)
   else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

#Function PODELI requires two statements
#one is the first statement
#two is the second statement
#the function reterns quotient of statements one and two
def podeli(one,two):
    if CORRECT_IN(one,two) is True:
        return round(one/two, 8)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0


#Function FAKTORIAL requirs two statements
#cislo number is an operand that is in the factorial
#function returns factorial of number
def faktorial(cislo):
    if CORRECT_IN(cislo,cislo) is True:
      if (cislo < 0):
         return None
      else if (cislo = 0) :
          return 1
      else:
        for i in range(1,cislo+1):
         odpoved *= i
      return round(odpoved, 8)
    else:
        raise TypeError("Wrong input! Please write a number.")
        return 0

#Function EXPONENTA requirs two statements
#operand osnova is a base (number) (cislo), 
# which is amplified
# exponenta is the **************
#The function returns the base raised to the power
def exponenta(osnova,stupen):
    if CORRECT_IN(osnova,stupen) is True:
     if (stupen == 0 or stupen < 0) and osnova == 0:
         raise TypeError("Wrong input! Please write a number stupen >0.")
     else:
         return round(osnova**stupen, 8)
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
            return round(osnova**(1/stupen), 8)
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
    
