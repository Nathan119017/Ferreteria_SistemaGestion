from django import forms
from .models import *
from django.contrib.auth.models import User

class FormSuppliers(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ['nombre', 'apellido', 'nombre_de_empresa', 'telefono', 'direccion', 'correo_electronico']
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre. Ejem. Mario Luis'  }),
                'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Apellido. Ejem. Aguirre Gutierrez'  }),
                'nombre_de_empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre de la empresa. Ejem. EjemComp' } ), 
                'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Numero de Telefono. Ejem. 12345678' }),
                'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la direccion de la empresa, Ejem. C. Mario Jaar, Tegucigalpa, Francisco Morazán'  }), 
                'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electronico. Ejem. ejem@gmail.com' }), 
                }
    
    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data['correo_electronico']
        return correo_electronico.lower()
