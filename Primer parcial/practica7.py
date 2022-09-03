"""
    PRACTICAS UNIDAD 1
    EQUIPO 4

    Integrantes:
    Alan Peña Ortiz 19100234
    Alan Abiud Castro Cruz 19100159
    Carlos Daniel Morín Rábago 19100222


    Practica 7 -Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir 
    YYYY/MM/DD” la segunda “2.- Imprimir  MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha 
    del día de hoy en el formato seleccionado.   
"""
from datetime import date
opcion = int(input('1.- Imprimir YYYY/MM/DD\n2.- Imprimir MM/DD/YYYY\n'))
print(date.today().strftime("%d/%m/%y" if opcion == 1 else "%m/%d/%y"))