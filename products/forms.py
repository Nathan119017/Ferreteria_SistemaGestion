from django import forms
from .models import *
from django.contrib.auth.models import User

class FormProducts(forms.ModelForm):
    has_expiry_date = forms.BooleanField(required=False, label='¿Tiene fecha de vencimiento?')
    fecha_de_vencimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Products
        fields = ['nombre', 'descripcion', 'fecha_de_vencimiento', 'precio', 'categoria', 'proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre del producto. Ejem. Martillo de Hierro'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Descripcion del producto. Ejem. 12 pulgadas, marca: "PRETUL"'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),  
        }

    def clean(self):
        cleaned_data = super().clean()
        has_expiry_date = cleaned_data.get('has_expiry_date')
        fecha_de_vencimiento = cleaned_data.get('fecha_de_vencimiento')

        if not has_expiry_date and fecha_de_vencimiento:
            raise forms.ValidationError('No puede especificar una fecha de vencimiento si no ha marcado la casilla correspondiente.')

        return cleaned_data

