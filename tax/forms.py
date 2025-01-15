from django import forms
from .models import Tax
from django.contrib.auth.models import User


class FormTax(forms.ModelForm):
    class Meta:
        model = Tax
        fields = ['nombre', 'tasa']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del impuesto'}),
            'tasa': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la tasa del impuesto'}),
        }
