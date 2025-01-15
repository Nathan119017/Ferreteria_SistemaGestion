from django import forms
from .models import Devolucion_History
from datetime import datetime, timedelta



class FormDevolucion_History(forms.ModelForm):
    class Meta:
        model = Devolucion_History
        fields = ['foranea', 'nombre_producto_cambio', 'cantidad_retornada_cambio']
        widgets = {
                'foranea': forms.Select(attrs={'class': 'form-control'}),
                'nombre_producto_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'cantidad_retornada_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                }

