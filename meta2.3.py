
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:08:35 2024

@author: zairapinon
"""

diccionario={}
print(diccionario)

print("--------Menu--------")
print("1- Agregar elemento")
print("2- Borrar elemento")
print("3- Mostrar diccionario")
print("4- Modificar elemento")
print("5- Salir")
print("--------------------")
o=int(input("escoge una opcion:"))

while o != 5:
    if o==1:
        a=input("Agregre una palabra:")
        b=input("Agregre usu significado:")
        diccionario[a] = b
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar diccionario")
        print("4- Modificar elemento")
        print("5- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
        
    elif o==2:
        r=input("escoge una opcion para eliminar:")
        valor_eliminado=diccionario.pop(r)
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar diccionario")
        print("4- Modificar elemento")
        print("5- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
        
    elif o==3:
        print(diccionario)
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar diccionario")
        print("4- Modificar elemento")
        print("5- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
        
    elif o==4:
        c=0
        a=input("Agregre una palabra:")
        b=input("Agregre usu significado:")
        diccionario[a] = b
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar diccionario")
        print("4- Modificar elemento")
        print("5- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
    
    else:
        print("opcion no valida")
        print("--------Menu--------")
        print("1- Agregar elemento")
        print("2- Borrar elemento")
        print("3- Mostrar diccionario")
        print("4- Modificar elemento")
        print("5- Salir")
        print("--------------------")
        o=int(input("escoge una opcion:"))
print("Adios")