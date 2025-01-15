from django import forms
from .models import Tax_History
from datetime import datetime, timedelta



class FormTax_History(forms.ModelForm):
    class Meta:
        model = Tax_History
        fields = ['foranea', 'nombre_cambio', 'tasa_cambio']
        widgets = {
                'foranea': forms.Select(attrs={'class': 'form-control'}),
                'nombre_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'tasa_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                }

