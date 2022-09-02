class Alumno:
    def __init__(self, usuario, contrasena, nombre, curp, ciudad,  rol = "Cliente"):
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol
        self.nombre = nombre
        self.curp = curp
        self.ciudad = ciudad

