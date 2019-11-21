#!/usr/bin/env python
# -*- coding: utf-8 -*-




def main(args):
    start= stop= 0
    while start<1:
        start= int(input('Podaj liczbę m: '))
    while stop < 1 or stop <= start:
        stop= int(input('Podaj liczbę n: '))
    for i in range(start, stop+1):
            print(i, '', end = '')
    else:
    
       print("Spadówa")
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
