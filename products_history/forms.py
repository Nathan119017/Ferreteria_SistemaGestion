from django import forms
from .models import Products_History
from datetime import datetime, timedelta



class FormProducts_History(forms.ModelForm):
    class Meta:
        model = Products_History
        fields = ['foranea', 'nombre_cambio', 'descripcion_cambio', 'fecha_de_vencimiento_cambio', 'stock_cambio', 'precio_cambio', 'categoria_cambio', 'proveedor_cambio']
        widgets = {
                'foranea': forms.Select(attrs={'class': 'form-control'}),
                'nombre_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'descripcion_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'fecha_de_vencimiento_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'stock_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'precio_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'categoria_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'proveedor_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                }

