from django.shortcuts import get_object_or_404, redirect, render
from Categoria.forms import CategoriaForm
from Categoria.models import Categoria

def detalleCategoria(req, id) :
    categoria = get_object_or_404(Categoria, pk = id);
    return render(req, 'DetalleCategoria.html', {'categoria': categoria});

def nuevoCategoria(req) :
    if req.method == "POST":
        formaCategoria = CategoriaForm(req.POST);

        if formaCategoria.is_valid():
            formaCategoria.save();
            return redirect('categoriaList');
    else:
        formaCategoria = CategoriaForm();
        return render(req, 'AgregarCategoria.html', {'formaCategoria': formaCategoria})

def editarCategoria(req, id):
    categoria = get_object_or_404(Categoria, pk = id);
    if req.method == "POST":
        formaCategoria = CategoriaForm(req.POST, instance = categoria);

        if formaCategoria.is_valid():
            formaCategoria.save();
            return redirect('categoriaList');
    else:
        formaCategoria = CategoriaForm(instance = categoria);
        return render(req, 'EditarCategoria.html', {'formaCategoria': formaCategoria})

def eliminarCategoria(req, id):
    categoria = get_object_or_404(Categoria, pk = id);
    if categoria:
        categoria.delete();
        return redirect('categoriaList');