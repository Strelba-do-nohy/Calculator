#IVS_project_2_kalkulacka
#matematicka knihovna
#strelba_do_nohy
#Dinara_Garipova xgarip00
#Datum 01.04.2022

#function CORRECT_IN Kontroluje, 
# zda uživatel zadává číslice, 
#a pokud ne, nepočítá


def CORRECT_IN(one,two):
    if (type(one) != int or type(one) != float):
        return False
    elif (type(two) != float or type(two) != int):
        return False
    else:
        return True

#funkce PLUS potrebuje dva operandy
#one je prvni operand
#two je druhy operand
#funkce vrati soucet operandu one a two
def PLUS(one,two):
    if CORRECT_IN(one,two) is True:
        return one+two
    else:
        raise ValueError
        return 0
        

#funkce MINUS potrebuje dva operandy
#one je prvni operand
#two je druhy operand
#funkce vrati odcitani operandu one a two
def MINUS(one,two):
    if CORRECT_IN(one,two) is True:
        return one-two
    else:
        raise ValueError
        return 0

#funkce UMNOZ potrebuje dva operandy
#one je prvni operand
#two je druhy operand
#funkce vrati soucin operandu one a two
def UMNOZ(one,two):
   if CORRECT_IN(one,two) is True:
        return one*two
   else:
        raise ValueError
        return 0

#funkce PODELI potrebuje dva operandy
#one je prvni operand
#two je druhy operand
#funkce vrati rozdil operandu one a two
def PODELI(one,two):
    if CORRECT_IN(one,two) is True:
        return one/two
    else:
        raise ValueError
        return 0


#funcke FAKTORIAL potrebuje jeden operand
#cislo je operand ktery je v faktorialu
#funkce vrati faktorial cisla
def FAKTORIAL(cislo):
    if CORRECT_IN(cislo,cislo) is True:
     if cislo >=0:
         return 1
         odpoved=1
     else:
         raise ValueError
     for i in range(1,cislo+1):
         odpoved *= i
     return odpoved
    else:
        raise ValueError
        return 0

#funkce EXPONENTA potrebuje dva operandy
#oberand osnova je základ (cislo), 
# ktery je umocnen
# exponenta je samotný stupeň
#Funkce vrací základ zvednutý na mocninu
def EXPONENTA(osnova,exponenta):
    if CORRECT_IN(osnova,exponenta) is True:
     if (exponenta == 0 or exponenta < 0) and osnova == 0:
         raise ValueError
     else:
         return osnova**exponenta
    else:
        raise ValueError
        return 0


#funkce KOREN potrebuje dva operandy
#osnova je cislo ze ktereho se bere koren
#stupen je korenovy stupen
#funkce vraci nejaky koren cisla
def KOREN(osnova,stupen):
    if CORRECT_IN(osnova,stupen) is True:
        if (stupen == 0 or stupen <0) and osnova ==0:
            raise ValueError
        else:
            if osnova<0:
                if stupen%2==1:
                    osnova=osnova*(-1)
                    return -1*osnova**(1/b)
                else:
                    raise ValueError
            return osnova**(1/stupen)
    else:
        raise ValueError
        return 0


#funkce LOG potrebuje dva operandy
#osnova je cislo 
#cislo je cislo s ktereho berem logarifm od osnovy
#funkce vraci nejaky logarifm cisla od osnovy
def LOG(osnova,cislo):
    if CORRECT_IN(osnova,cislo) is True:
        for i in range(1,cislo):
         if osnova**i==cislo:
             return i
    else:
        raise ValueError
        return 0
    
