#IVS_project2_kalkulacka
#profiling
#strelba_do_nohy
#Garipova Dinara xgarip00
#Datum 17.04.2022

import matematicka_knihovna as mk
from sys import *

pocet = 0
cisla = input().split()
classic_add = 0.0
exponenta_add = 0.0

for i in cisla:
    classic_add = mk.plus(classic_add,i)
    exponenta_add = mk.plus(exponenta_add, mk.exponenta(i,2))
    pocet = mk.plus(pocet,i)

if (pocet == 0):
    print(0)
    exit()

middle = mk.podeli(classic_add, pocet)
odpoved = mk.koren(mk.minus(mk.umnoz(exponenta_add, mk.umnoz(pocet, mk.exponenta(middle,2))), mk.minus(pocet,1)))

print(odpoved)