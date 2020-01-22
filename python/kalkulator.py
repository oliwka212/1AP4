#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kalkulator.py
#  
wynik= 0


def druj():
    global suma
    print(suma)
    suma = 20
    
def drukuj2(liczba):
    liczba += 10
    print(liczba)
    return liczba
    
def main(args):
    suma = 5 # zmienna lokalna
    liczba = 3
    #print(suma)
    #drukuj()
    #print (]])
    print(liczba)
    liczba = drukuj2(liczba)
    print(liczba)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
