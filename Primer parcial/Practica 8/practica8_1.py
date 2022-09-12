class Usuario:
    def __init__(self, username, contrasena, nombre, curp, ciudad,  rol = "Cliente"):
        self.username = username
        self.contrasena = contrasena
        self.rol = rol
        self.nombre = nombre
        self.curp = curp
        self.ciudad = ciudad


    def __str__(self):
        return f"Username: {self.username} Rol: {self.rol} Nombre: {self.nombre}  CURP: {self.curp} Ciudad: {self.ciudad}"
    
