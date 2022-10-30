from django.db import models
from Categoria.models import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length = 255);
    descripcion = models.CharField(max_length = 255);
    fechaIngreso = models.DateField();
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null = True);
    precio = models.FloatField();

    def __str__(self) -> str:
        return f'Producto {self.id}: {self.nombre} ${self.precio}';
