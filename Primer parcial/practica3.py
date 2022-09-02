# 3 Entrada de datos y manipulación. 
# Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de 
# manera inversa letra por letra

nombre = input('Dame tu nombre: ')
nombre = list(nombre)
nombre.reverse()
for i in nombre:
    print(i)