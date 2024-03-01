#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:58:06 2024

@author: zairapinon
"""

n=float(input("ingrese la calificacion:"))

if n>=0 and n<=100:
    if n>=60 and n<=100:
        if n == 100:
            print("excelente")
        elif n>=90 and n<=99.9:
            print("Muy bien")
        elif n>=80 and n<=89.9:
            print("bien")
        elif n>=70 and n<=79.9:
            print("regular")
        else:
            print("suficiente")
    else:
        print("reprobaste")
else:
    print("opcion no valida")