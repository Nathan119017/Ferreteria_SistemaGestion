from django import forms
from .models import *
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class FormClients(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormClients, self).__init__(*args, **kwargs)
        self.fields['metodos_pago'].queryset = Payment_Methods.objects.all()
    

    class Meta:
        model = Clients
        fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'direccion', 'correo_electronico', 'metodos_pago']
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre. Ejem. Mario Luis' }),
                'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Apellido. Ejem. Aguirre Gutierrez' }),
                'fecha_de_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type':"date"}),
                'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la direccion de la empresa, Ejem. C. Mario Jaar, Tegucigalpa, Francisco Morazán'  }),
                'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electronico. Ejem. ejem@gmail.com' }), 
                'metodos_pago': forms.Select(attrs={'class': 'form-control'}),
                }
                
                
                
class FormClientsWithValidation(FormClients):
    
    def clean_fecha_de_nacimiento(self):
        fecha_de_nacimiento = self.cleaned_data['fecha_de_nacimiento']
        edad_minima = datetime.now().date() - timedelta(days=18 * 365)  # Se resta la edad mínima de 18 años en días
        if fecha_de_nacimiento > edad_minima:
            raise forms.ValidationError('El empleado debe tener al menos 18 años de edad.')
        return fecha_de_nacimiento
