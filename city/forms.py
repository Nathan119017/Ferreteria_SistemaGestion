from django import forms
from .models import City  # Cambio de Tax a City
from django.contrib.auth.models import User


class FormCity(forms.ModelForm):  # Cambio de FormTax a FormCity
    class Meta:
        model = City  # Cambio de Tax a City
        fields = ['nombre_ciudad', 'codigo_postal']  # Cambio de nombre de los campos
        widgets = {
            'nombre_ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la ciudad'}),  # Cambio de nombre del atributo
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código postal de la ciudad'}),  # Cambio de nombre del atributo
        }
