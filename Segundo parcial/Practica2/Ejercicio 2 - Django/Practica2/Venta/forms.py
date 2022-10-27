from django.forms import ModelForm, DateInput, NumberInput
from Venta.models import Venta

class VentaForm(ModelForm):
    class Meta:
        model = Venta;
        fields = '__all__';
        widgets = {
            'fechaIngreso': DateInput(attrs={'type': 'date'}),
            'cantidad': NumberInput(attrs={'type': 'number'})
        };