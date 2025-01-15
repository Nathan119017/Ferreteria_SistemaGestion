from django import forms
from .models import CAI


class FormCAI(forms.ModelForm):
    class Meta:
        model = CAI
        fields = ['nombre_empresa', 'cai']
        widgets = {
            'nombre_empresa': forms.Select(attrs={'class': 'form-control'}),
            'cai': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el CAI'}),
        }
