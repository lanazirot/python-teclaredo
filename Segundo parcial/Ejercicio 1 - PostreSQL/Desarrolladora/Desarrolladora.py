from logger_base import log
class Desarrolladora:
    def __init__(self, iddesarrolladora=None, nombre=None, pais=None, empleados=None) -> None:
        self._iddesarrolladora = iddesarrolladora
        self._nombre = nombre
        self._pais = pais
        self._empleados = empleados

    @property
    def iddesarrolladora(self):
        return self._iddesarrolladora

    @property
    def nombre(self):
        return self._nombre

    @property
    def pais(self):
        return self._pais

    @property
    def empleados(self):
        return self._empleados
    
    def __str__(self) -> str:
        return f"\nId Desarrolladora: {self._iddesarrolladora} \nNombre: {self._nombre} \nPais: {self._pais} \nEmpleados: {self._empleados} \n"