class Usuario:
    def __init__(self, username, contrasena, nombre, curp, ciudad,  rol = "Cliente"):
        self._username = username
        self._contrasena = contrasena
        self._rol = rol
        self._nombre = nombre
        self._curp = curp
        self._ciudad = ciudad


    def __str__(self):
        return f"({self.username}) ({self.rol}) ({self.nombre}) ({self.curp}) ({self.ciudad})"
    
    # Getters 
  
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def curp(self):
        return self._curp
    
    @property
    def ciudad(self):
        return self._ciudad
    
    @property
    def rol(self):
        return self._rol
    
    @property
    def contrasena(self):
        return self._contrasena
    
    # Setters

        
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @curp.setter
    def curp(self, curp):
        self._curp = curp
        
    @ciudad.setter
    def ciudad(self, ciudad):
        self._ciudad = ciudad
    
    @rol.setter
    def rol(self, rol):
        self._rol = rol
    
    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena