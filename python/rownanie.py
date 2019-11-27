#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Rozwiąż równanie liniowe a * x + b= 0
# 1)Pobierz wartości współczynników a i b
# 2) Jeśli a =0
#       Jeśli b = 0 wyprowadź nieskończenie wiele rozwiązań"
#       w przeciwnym wypadku: nie ma rozwiązania
#    w przeciwnym wypadku oblicz x = -b / a i wyprowadź x
# 


def main(args):
    a= int(input("Podaj liczbę a: "))
    b= int(input("Podaj liczbę b: "))
    
    if a==0:
        if b==0:
            print("nieskończenie wiele rozwiązań!")
        else:
            print("równanie sprzeczne")
    else:
        x = -b / a
        print(x)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
