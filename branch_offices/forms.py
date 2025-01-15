from django import forms
from .models import *
from django.contrib.auth.models import User


class FormBranch_Offices(forms.ModelForm):
    class Meta:
        model = Branch_Offices
        fields = ['nombre_sucursal', 'telefono', 'direccion', 'correo_electronico', 'ciudad']
        widgets = {
                'nombre_sucursal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre de la Sucursal. Ejem. Sucursal Lopez Perez' }),
                'telefono': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese el Numero de Telefono. Ejem. 12345678'}), 
                'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la direccion de la sucursal, Ejem. C. Mario Jaar, Tegucigalpa, Francisco Morazán'}),
                'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electronico. Ejem. ejem@gmail.com' }),
                'ciudad': forms.Select(attrs={'class': 'form-control'}), 
                }
                
