# Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el 
# producto total. 

def productoTotal(*numeros):
    res = 1
    for i in numeros:
        res = res * i
    return res

assert productoTotal(1,2,3) == 6
assert productoTotal(1,2,3,0) == 0


print('Pruebas pasadas :)')