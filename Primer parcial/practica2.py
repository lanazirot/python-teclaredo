# 2 Manejo y manipulación de elementos de una lista 
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
#  letras que ocupen 
# posiciones múltiplos de 3, y muestre por pantalla la lista resultante

abecedario = [chr(i) for i in range(65,91)]
abecedarioLimpio = [a for i,a in enumerate(abecedario) if i % 3 != 0]

assert len(abecedarioLimpio) == 17
assert len(abecedarioLimpio) < len(abecedario)

print(abecedarioLimpio)