# 5 Manejo de información 
# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato 
# “{llave}”: “{Valor}”

def formato(**params):
    for key, value in params.items():
        print(f' "{key}":"{value}" ')

formato(Nombre = "Alan", Apellido = "Ortiz")
formato(Nombre = "Alan", Apellido = "Castro")