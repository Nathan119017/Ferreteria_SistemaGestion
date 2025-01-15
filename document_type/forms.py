from django import forms
from .models import *
from django.contrib.auth.models import User


class FormDocument_Type(forms.ModelForm):
    class Meta:
        model = Document_Type
        fields = ['nombre', 'descripcion']
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre del tipo de documento.' }),
                'descripcion': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese la descripcion del documento'}), 
                }
                
