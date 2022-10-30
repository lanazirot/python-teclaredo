from django.forms import ModelForm, DateInput, NumberInput
from Producto.models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto;
        fields = '__all__';
        widgets = {
            'fechaIngreso': DateInput(attrs={'type': 'date'}),
            'precio': NumberInput(attrs={'type':'number'})
        };