from Videojuego import Videojuego
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class VideojuegoDao:
    _SELECCIONAR = "SELECT * FROM videojuego ORDER BY idvideojuego"
    _INSERTAR = "INSERT INTO videojuego(titulo,genero,precio) Values(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE videojuego SET titulo=%s,genero=%s,precio=%s WHERE idvideojuego=%s"
    _ELIMINAR = "DELETE FROM videojuego WHERE idvideojuego=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                videojuegos=[]
                for r in registros:
                    videojuego = Videojuego(r[0],r[1],r[2],r[3])
                    videojuegos.append(videojuego)
                return videojuegos

    @classmethod
    def insertar(cls,Videojuego):
        with CursorDelPool() as cursor:
            valores = (Videojuego.titulo, Videojuego.genero, Videojuego.precio)
            cursor.execute(cls._INSERTAR,valores)
            log.debug("Se registro el videojuego")
            return cursor.rowcount

    @classmethod
    def actualizar(cls,Videojuego):
        with CursorDelPool() as cursor:
            valores = (Videojuego.titulo,Videojuego.genero, Videojuego.precio,Videojuego.idvideojuego)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug("Se actualizo el videojuego")
            return cursor.rowcount

    @classmethod
    def eliminar(cls,Videojuego):
        with CursorDelPool() as cursor:
            valores = (Videojuego.idvideojuego,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug("Se elimino el videojuego")
            return cursor.rowcount

if __name__=="__main__":
    
    #Insertar
    videojuegos = Videojuego(idvideojuego=1,titulo="FIFA 23",genero="Deportes",precio="1200")
    videojuegosInsertados = VideojuegoDao.insertar(videojuegos)
    log.debug(f"Videojuegos insertados {videojuegosInsertados}")
    
    #Actualizar
    videojuego1=Videojuego(idvideojuego=2,titulo="Call of Duty Modern Warfare 2",genero="Shooter",precio="1400")
    videojuegosActualizados = VideojuegoDao.actualizar(videojuego1)
    log.debug(f"Videojuegos actualizadas {videojuegosActualizados}")
    
    #Eliminar
    videojuego1=Videojuego(idvideojuego=3)
    videojuegosEliminados = VideojuegoDao.eliminar(videojuego1)
    log.debug(f"Videojuegos eliminados {videojuegosEliminados}")
    
    #Ver
    videojuegos = VideojuegoDao.seleccionar()
    for p in videojuegos:
        log.debug(p)