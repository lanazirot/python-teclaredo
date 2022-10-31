from Desarrolladora import Desarrolladora
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class DesarrolladoraDao:
    _SELECCIONAR = "SELECT * FROM desarrolladora ORDER BY iddesarrolladora"
    _INSERTAR = "INSERT INTO desarrolladora(nombre,pais,empleados) Values(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE desarrolladora SET nombre=%s,pais=%s,empleados=%s WHERE iddesarrolladora=%s"
    _ELIMINAR = "DELETE FROM desarrolladora WHERE iddesarrolladora=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                desarrolladoras=[]
                for r in registros:
                    desarrolladora = Desarrolladora(r[0],r[1],r[2],r[3])
                    desarrolladoras.append(desarrolladora)
                return desarrolladoras

    @classmethod
    def insertar(cls,Desarrolladora):
        with CursorDelPool() as cursor:
            valores = (Desarrolladora.nombre, Desarrolladora.pais, Desarrolladora.empleados)
            cursor.execute(cls._INSERTAR,valores)
            log.debug("Se registro la desarrolladora")
            return cursor.rowcount

    @classmethod
    def actualizar(cls,Desarrolladora):
        with CursorDelPool() as cursor:
            valores = (Desarrolladora.nombre,Desarrolladora.pais, Desarrolladora.empleados,Desarrolladora.iddesarrolladora)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug("Se actualizo la desarrolladora")
            return cursor.rowcount

    @classmethod
    def eliminar(cls,Desarrolladora):
        with CursorDelPool() as cursor:
            valores = (Desarrolladora.iddesarrolladora,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug("Se elimino la desarrolladora")
            return cursor.rowcount

if __name__=="__main__":
    
    #Insertar
    desarrolladoras = Desarrolladora(iddesarrolladora=1,nombre="FROM SOFTWARE",pais="Japon",empleados="2500")
    desarrolladorasInsertadas = DesarrolladoraDao.insertar(desarrolladoras)
    log.debug(f"Desarrolladoras insertadas {desarrolladorasInsertadas}")
    
    #Actualizar
    desarrolladora1=Desarrolladora(iddesarrolladora=2,nombre="SUDA 51",pais="Japon",empleados="800")
    desarrolladorasActualizadas = DesarrolladoraDao.actualizar(desarrolladora1)
    log.debug(f"Desarrolladoras actualizadas {desarrolladorasActualizadas}")
    
    #Eliminar
    desarrolladora1=Desarrolladora(iddesarrolladora=3)
    desarrolladorasEliminadas = DesarrolladoraDao.eliminar(desarrolladora1)
    log.debug(f"Desarrolladoras eliminadas {desarrolladorasEliminadas}")
    
    #Ver
    desarrolladoras = DesarrolladoraDao.seleccionar()
    for p in desarrolladoras:
        log.debug(p)