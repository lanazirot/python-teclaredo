from practica8_1 import Usuario


listaUsuarios = {}

def registrarUsuario():
    print('------------Registro de usuario------------')
    username = input('Username')
    contrasena = input('Password: ')
    nombre = input('Nombre real: ')
    ciudad = input('Ciudad de nacimiento: ')
    curp = input('Curp: ')
    
    nuevoUsuario = Usuario(username, contrasena, nombre, curp, ciudad)
    
    if nuevoUsuario.curp in listaUsuarios:
        print ('Usuario ya existe en los registros!')
    else:
        listaUsuarios[nuevoUsuario.curp] = nuevoUsuario
        menu()
    
def iniciarSesion():
    print('------------Inicio de sesion------------')

def menu():
    opcion = int(input('1.- Registro\n2.- Inicio de sesion\n3.- Salida'))
    if opcion not in [1,2,3]:
        print('Opcion invalida, ingrese una opcion del 1 al 3')
        menu()
    else:
        if opcion == 1:
            registrarUsuario()
        elif opcion == 2:
            iniciarSesion()
        elif opcion == 3:
            print('Gracias por usar el programa')
            exit()
    
    

if __name__ == '__main__':
    menu()