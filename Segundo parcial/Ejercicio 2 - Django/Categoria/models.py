from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length = 255);
    descripcion = models.CharField(max_length = 255);
    fechaIngreso = models.DateField();

    def __str__(self) -> str:
        return f'Categoria {self.id}: {self.nombre}';
