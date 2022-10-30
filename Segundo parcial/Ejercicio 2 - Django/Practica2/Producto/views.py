from django.shortcuts import get_object_or_404, redirect, render
from Producto.forms import ProductoForm
from Producto.models import Producto

def detalleProducto(req, id) :
    producto = get_object_or_404(Producto, pk = id);
    return render(req, 'DetalleProducto.html', {'producto': producto});

def nuevoProducto(req) :
    if req.method == "POST":
        formaProducto = ProductoForm(req.POST);

        if formaProducto.is_valid():
            formaProducto.save();
            return redirect('productoList');
    else:
        formaProducto = ProductoForm();
        return render(req, 'AgregarProducto.html', {'formaProducto': formaProducto})

def editarProducto(req, id):
    producto = get_object_or_404(Producto, pk = id);
    if req.method == "POST":
        formaProducto = ProductoForm(req.POST, instance = producto);

        if formaProducto.is_valid():
            formaProducto.save();
            return redirect('productoList');
    else:
        formaProducto = ProductoForm(instance = producto);
        return render(req, 'EditarProducto.html', {'formaProducto': formaProducto})

def eliminarProducto(req, id):
    producto = get_object_or_404(Producto, pk = id);
    if producto:
        producto.delete();
        return redirect('productoList');