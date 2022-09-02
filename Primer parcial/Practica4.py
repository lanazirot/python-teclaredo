"""
    Equipo 4.

    Practica 4: Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture 
    las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato 
    “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre
"""

def imprimirMenu() :
    print("\n \nSeleccione una opcion del siguiente menu:")
    print("[0] - Salir")
    print("[1] - Ingresar materia")
    return int(input("Valor seleccionado: "));

def agregarMateria() :
    mNombre = input("\nIngrese el nombre de la materia: ");
    mCreditos = input("Ingrese la cantidad de creditos para la materia: ");
    miReticula[mNombre] = int(mCreditos);
    print("");

miReticula = {};
selectorDeOpcion = 1;

while(selectorDeOpcion != 0) :
    selectorDeOpcion = imprimirMenu();
    if selectorDeOpcion == 1 :
        agregarMateria();

print("\n++--Programa finalizado--++")
if not miReticula :
    print("No se econtraron materias registradas.");
else :    
    print("Resumen de materias registradas:");    
    sumaDeCreditos = 0;
    for materia in miReticula :
        print(f"   - {materia} tiene {miReticula.get(materia)} creditos.");
        sumaDeCreditos += miReticula.get(materia);
    print(f"El total de creditos es de: {sumaDeCreditos}");
    print("++-----------------------++");