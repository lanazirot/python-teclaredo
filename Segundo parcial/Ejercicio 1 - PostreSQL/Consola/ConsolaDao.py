from Consola import Consola
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class ConsolaDao:
    _SELECCIONAR = "SELECT * FROM consola ORDER BY idconsola"
    _INSERTAR = "INSERT INTO consola(nombre,empresa,precio) Values(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE consola SET nombre=%s,empresa=%s,precio=%s WHERE idconsola=%s"
    _ELIMINAR = "DELETE FROM consola WHERE idconsola=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                consolas=[]
                for r in registros:
                    consola = Consola(r[0],r[1],r[2],r[3])
                    consolas.append(consola)
                return consolas

    @classmethod
    def insertar(cls,Consola):
        with CursorDelPool() as cursor:
            valores = (Consola.nombre, Consola.empresa, Consola.precio)
            cursor.execute(cls._INSERTAR,valores)
            log.debug("Se registro la consola")
            return cursor.rowcount

    @classmethod
    def actualizar(cls,Consola):
        with CursorDelPool() as cursor:
            valores = (Consola.nombre,Consola.empresa, Consola.precio,Consola.idconsola)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug("Se actualizo la consola")
            return cursor.rowcount

    @classmethod
    def eliminar(cls,Consola):
        with CursorDelPool() as cursor:
            valores = (Consola.idconsola,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug("Se elimino la consola")
            return cursor.rowcount

if __name__=="__main__":
    
    #Insertar
    #consolas = Consola(idconsola=1,nombre="Xbox Series X",empresa="Microsoft",precio="15000")
    #consolasInsertadas = ConsolaDao.insertar(consolas)
    #log.debug(f"Consolas insertadas {consolasInsertadas}")
    
    #Actualizar
    #consola1=Consola(idconsola=2,nombre="Xbox Series S",empresa="Microsoft",precio="6000")
    #consolasActualizadas = ConsolaDao.actualizar(consola1)
    #log.debug(f"Consolas actualizadas {consolasActualizadas}")
    
    #Eliminar
    #consola1=Consola(idconsola=3)
    #consolasEliminadas = ConsolaDao.eliminar(consola1)
    #log.debug(f"Consolas eliminadas {consolasEliminadas}")
    
    #Ver
    consolas = ConsolaDao.seleccionar()
    for p in consolas:
        log.debug(p)