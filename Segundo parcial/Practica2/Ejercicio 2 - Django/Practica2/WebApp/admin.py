from django.contrib import admin
from Usuario.models import Usuario
from Categoria.models import Categoria
from Producto.models import Producto
from Venta.models import Venta

admin.site.register(Usuario);
admin.site.register(Categoria);
admin.site.register(Producto);
admin.site.register(Venta);