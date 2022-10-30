from django.db import models
from Producto.models import Producto

class Venta(models.Model):
    descripcion = models.CharField(max_length = 255);
    fechaIngreso = models.DateField();
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null = True);
    cantidad = models.IntegerField();