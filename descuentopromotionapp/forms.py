from django import forms
from .models import PromDisc

class FormDiscP(forms.ModelForm):
    class Meta:
        model = PromDisc
        fields = ['nombrepromocion_descuento', 'porcentaje', 'promocion_descuento']
        widgets = {
            'nombrepromocion_descuento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre de el Descuento o Promocion Ejem. Promocion Navideña' }),
            'porcentaje': forms.Select(attrs={'class': 'form-control'}), 
            'promocion_descuento': forms.Select(attrs={'class': 'form-control'}), 
        }