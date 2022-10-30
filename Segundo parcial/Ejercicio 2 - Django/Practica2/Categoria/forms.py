from django.forms import ModelForm, DateInput
from Categoria.models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria;
        fields = '__all__';
        widgets = {
            'fechaIngreso': DateInput(attrs={'type': 'date'})
        };