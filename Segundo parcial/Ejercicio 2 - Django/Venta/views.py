from django.shortcuts import get_object_or_404, redirect, render
from Venta.forms import VentaForm
from Venta.models import Venta

def detalleVenta(req, id) :
    venta = get_object_or_404(Venta, pk = id);
    return render(req, 'DetalleVenta.html', {'venta': venta});

def nuevoVenta(req) :
    if req.method == "POST":
        formaVenta = VentaForm(req.POST);

        if formaVenta.is_valid():
            formaVenta.save();
            return redirect('ventaList');
    else:
        formaVenta = VentaForm();
        return render(req, 'AgregarVenta.html', {'formaVenta': formaVenta})

def editarVenta(req, id):
    venta = get_object_or_404(Venta, pk = id);
    if req.method == "POST":
        formaVenta = VentaForm(req.POST, instance = venta);

        if formaVenta.is_valid():
            formaVenta.save();
            return redirect('ventaList');
    else:
        formaVenta = VentaForm(instance = venta);
        return render(req, 'EditarVenta.html', {'formaVenta': formaVenta})

def eliminarVenta(req, id):
    venta = get_object_or_404(Venta, pk = id);
    if venta:
        venta.delete();
        return redirect('ventaList');