from django import forms
from .models import OrderDetail
from datetime import datetime, timedelta

class FormOrderDetail(forms.ModelForm):
    class Meta:
        model = OrderDetail
        exclude = [''] 
        fields = ['num_order', 'nombre_product', 'cantidad', 'descripcion', 'precio_unitario',]
        widgets = {
            'num_order': forms.Select(attrs={'class': 'form-control'}),
            'nombre_product': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Descripcion del Pedido' }),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
        }
        
     
    

