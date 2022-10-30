from django.contrib import admin
from django.urls import path
from Usuario.views import detalleUsuario, nuevoUsuario, eliminarUsuario, editarUsuario
from WebApp.views import usuarioView, mainView, categoriaView, productoView, ventaView
from Categoria.views import detalleCategoria, nuevoCategoria, eliminarCategoria, editarCategoria
from Producto.views import detalleProducto, nuevoProducto, eliminarProducto, editarProducto
from Venta.views import detalleVenta, nuevoVenta, eliminarVenta, editarVenta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainView, name='index'),

    path('lista_usuarios', usuarioView, name='usuarioList'),
    path('detalle_usuario/<int:id>', detalleUsuario),
    path('nuevo_usuario', nuevoUsuario),
    path('editar_usuario/<int:id>', editarUsuario),
    path('eliminar_usuario/<int:id>', eliminarUsuario),
    
    path('lista_categorias', categoriaView, name='categoriaList'),
    path('detalle_categoria/<int:id>', detalleCategoria),
    path('nuevo_categoria', nuevoCategoria),
    path('editar_categoria/<int:id>', editarCategoria),
    path('eliminar_categoria/<int:id>', eliminarCategoria),

    path('lista_productos', productoView, name='productoList'),
    path('detalle_producto/<int:id>', detalleProducto),
    path('nuevo_producto', nuevoProducto),
    path('editar_producto/<int:id>', editarProducto),
    path('eliminar_producto/<int:id>', eliminarProducto),

    path('lista_ventas', ventaView, name='ventaList'),
    path('detalle_venta/<int:id>', detalleVenta),
    path('nuevo_venta', nuevoVenta),
    path('editar_venta/<int:id>', editarVenta),
    path('eliminar_venta/<int:id>', eliminarVenta),
]
