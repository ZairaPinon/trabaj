#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:19:52 2024

@author: zairapinon
"""

lista=["Juan","Pedro","Danna"]



print("--------Menu--------")
print("1- Agregar elemento")
print("2- Borrar elemento")
print("3- Mostrar lista")
print("4- Salir")
print("--------------------")
o=int(input("escoge una opcion:"))

while o != 4:
    if o==1:
        a=input("Agregre un nombre:")
        lista.append(a)
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar lista")
        print("4- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
    elif o==2:
        r=int(input("escoge una opcion para eliminar:"))
        lista.pop(r)
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar lista")
        print("4- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
    elif o==3:
        for elemento in lista:
            print(elemento)
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar lista")
        print("4- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
    
    else:
        print("opcion no valida")
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar lista")
        print("4- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
print("Adios")

