"""
    PRACTICAS UNIDAD 1
    EQUIPO 4

    Integrantes:
    Alan Peña Ortiz 19100234
    Alan Abiud Castro Cruz 19100159
    Carlos Daniel Morín Rábago 19100222


    Practica 6 -Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar 
    condicionales, máximo 5 líneas de código.   

"""
baseDeDatos = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince", 16: "dieciseis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve", 20: "veinte"};
lectura = int(input("Ingresa un numero del 1 al 20: "));

if lectura > 20 or lectura < 1 : 
    print("El numero no se encuentra en el rango del 1 al 20.");
else : 
    print(baseDeDatos.get(lectura));