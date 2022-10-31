from logger_base import log
class Consola:
    def __init__(self, idconsola=None, nombre=None, empresa=None, precio=None) -> None:
        self._idconsola = idconsola
        self._nombre = nombre
        self._empresa = empresa
        self._precio = precio

    @property
    def idconsola(self):
        return self._idconsola

    @property
    def nombre(self):
        return self._nombre

    @property
    def empresa(self):
        return self._empresa

    @property
    def precio(self):
        return self._precio
    
    def __str__(self) -> str:
        return f"\nId Consola: {self._idconsola} \nNombre: {self._nombre} \nEmpresa: {self._empresa} \nPrecio: {self._precio} \n"