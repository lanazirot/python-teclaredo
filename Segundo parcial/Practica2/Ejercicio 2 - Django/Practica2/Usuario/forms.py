from django.forms import ModelForm, EmailInput, DateInput
from Usuario.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario;
        fields = '__all__';
        widgets = {
            'correoElectronico': EmailInput(attrs={'type': 'email'}),
            'fechaIngreso': DateInput(attrs={'type': 'date'})
        };