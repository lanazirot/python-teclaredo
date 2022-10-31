from logger_base import log
class Videojuego:
    def __init__(self, idvideojuego=None, titulo=None, genero=None, precio=None) -> None:
        self._idvideojuego = idvideojuego
        self._titulo = titulo
        self._genero = genero
        self._precio = precio

    @property
    def idvideojuego(self):
        return self._idvideojuego

    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def precio(self):
        return self._precio
    
    def __str__(self) -> str:
        return f"\nId Videojuego: {self._idvideojuego} \nTitulo: {self._titulo} \nGenero: {self._genero} \nPrecio: {self._precio} \n"