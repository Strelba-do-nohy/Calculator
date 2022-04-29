########################################################
# Project name: Profiling for calculator
# Package: Calculator
# File: profiling.py
# Date: 10.04.2022
# Last changes: 28.04.2022
# Author: Strelba do nohy (Dinara Garipova -- xgarip00)
#########################################################
# @package Calculator
# @file profiling.py
# @author Strelba do nohy (Dinara Garipova -- xgarip00)
##########################################################

# @brief To import all functions from math library and to name math library as "mk"
# @brief To import all functions from sys
import cProfile, pstats
import matematicka_knihovna as mk


# @param pocet-counter of inputting numbers (flag for the next functon)
pocet = 0
# @param cisla-array of all inputting numbers
cisla = input().replace("\t", " ").replace("\n", " ").split(" ")


profile = cProfile.Profile()
profile.enable()

# @param classic_add - counter of sum of inputting numbers (like E(i=1,N)x(i))
classic_add = 0
# @param exponenta_add - counter of squared sum of inputting numbers
exponenta_add = 0

# @brief counting sum of inputting numbers (classic_add), squared sum (exponenta_add) and amount of inputting numbers
for i in cisla:
    classic_add = mk.plus(classic_add,float(i))
    exponenta_add = mk.plus(exponenta_add, mk.exponenta(float(i),2))
    pocet = mk.plus(pocet,1)

# @brief Checking if amount of all inputting numbers are 0 then write 0 to the screen
if (pocet == 0):
    print(0)
    exit()

# @param middle is the average of all inputting numbers
middle = mk.podeli(classic_add, pocet)
# @param odpoved is the result from the given expression(sample standard deviations)
odpoved = mk.koren(mk.minus(mk.umnoz(exponenta_add, mk.umnoz(pocet, mk.exponenta(middle,2))), mk.minus(pocet,1)),2)



profile.disable()
stats = pstats.Stats(profile).sort_stats('time')
stats.print_stats()
stats.dump_stats("profiling.prof")
######################################################################################################################################
#End of file profiling.py
#######################################################################################################################################