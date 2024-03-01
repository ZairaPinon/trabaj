#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:22:49 2024

@author: zairapinon
"""
op=0
def menu():
    print()
    print("Hola >:)")
    print()
    print("------------Menu------------")
    print("1- Centigrados a Fahrenheit")
    print("2- Positivo o negativo?")
    print("3- Par o impar?")
    print("4- Numeros a letras")
    print("5- Sumatoria de 5 numero")
    print("6- Salir")
    print("----------------------------")
    
def grados():
    c=float(input("pon los centigrados >:(  :"))
    f = ((c*1.8)+32)
    
    print("El Fahrenheit es >:(  :",f)
    return f
def moM():
    o=int(input("escoge un numero:"))
    if o>0:
        print("El numero es positivo :)")
    else:
        print("El numero es negativo :(")
def pon():
    x=int(input("escoge un numero:"))
    if x%2==0:
        print("El numero es par :)")
    else:
        print("El numero es impar :(")
def letras():
    n=int(input("escoge un numero entre el 1 y el 10:"))
    if n == 1:
        print("uno")
    elif n == 2:
        print("dos")
    elif n == 3:
        print("tres")
    elif n == 4:
        print("cuatro")
    elif n == 5:
        print("cinco")
    elif n == 6:
        print("seis")
    elif n == 7: 
        print("siete")
    elif n == 8:
        print("ocho")
    elif n == 9:
        print("nueve")
    elif n == 10:
        print("diez")
    else:
         print("opcion no valida")
def suma():
    a=int(input("pon un numero >:(  :"))
    b=int(input("pon otro numero >:(  :"))
    c=int(input("pon otro numero >:(  :"))
    d=int(input("pon otro numero >:(  :"))
    e=int(input("pon uno mas >:(  :"))
    s=a+b+c+d+e
    print("la suma es >:(  :",s)
    return s
        
while op != 6:
    menu()
    op=int(input("escoge una opcion:"))
    if op == 1:
        grados()
    elif op == 2:
        moM()
    elif op == 3:
        pon()
    elif op == 4:
        letras()
    elif op == 5:
        suma()
    else:
        print("opcion no valida")
print("Adios >:(")