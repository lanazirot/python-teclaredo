from practica8_1 import Usuario
import os

administrador = Usuario('Administrador', 'administrador', 'ADMIN001HTSXRLA3', 'Laredo', 'Administrador')

listaUsuarios = {}

def registrarUsuario():
    os.system('cls')
    print('------------Registro de usuario------------')
    username = input('Username: ')
    contrasena = input('Password: ')
    nombre = input('Nombre real: ')
    ciudad = input('Ciudad de nacimiento: ')
    curp = input('Curp: ')
    nuevoUsuario = Usuario(username, contrasena, nombre, curp, ciudad)
    for value in listaUsuarios.values():
        if value.curp == curp:
            print ('Usuario ya existe en los registros.')
            menu()
    listaUsuarios[nuevoUsuario.username] = nuevoUsuario 
    menu()
    
def iniciarSesion():
    os.system('cls')
    print('------------Inicio de sesion------------')
    username = input('Username: ')
    password = input('Password: ')
    
    if username in listaUsuarios:
        usuario = listaUsuarios[username]
        if usuario.contrasena == password:
            currentUser = listaUsuarios[username]
            if currentUser.rol == 'Administrador':
                print('----------------Lista de usuarios----------------')
                print(listaUsuarios)
            else:
                print(currentUser)
        else:
            print("Datos incorrectos")
            menu()
    else:
        print("Cuenta inexistente")
        menu()
    

def menu():
    os.system('cls')
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
            os.system('cls')
            print('Gracias por usar el programa')
            exit()
    
    

if __name__ == '__main__':
    listaUsuarios[administrador.username] = administrador
    menu()