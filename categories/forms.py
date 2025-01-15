from django import forms
from .models import *
from django.contrib.auth.models import User


class FormCategories(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['nombre', 'descripcion']
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre. Ejem. Herramienta' }),
                'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripcion de la categoria. Ejem. Utiles de contruccion' }),
                }
                
