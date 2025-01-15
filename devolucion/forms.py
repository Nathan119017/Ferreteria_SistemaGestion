from django import forms
from .models import Devolucion


class FormDevolucion(forms.ModelForm):
    class Meta:
        model = Devolucion
        fields = ['nombre_producto', 'cantidad_retornada']
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del producto'}),
            'cantidad_retornada': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad retornada'}),
        }
