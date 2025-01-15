from django import forms
from .models import Sale_History
from datetime import datetime, timedelta



class FormSale_History(forms.ModelForm):
    class Meta:
        model = Sale_History
        fields = ['foranea', 'cliente_cambio', 'producto_cambio', 'cantidad_producto_cambio', 'precio_venta_cambio', 'fecha_venta_cambio', 'metodo_pago_cambio', 'total_venta_cambio', 'sucursal_cambio', 'usuario_cambio', 'num_factura_cambio']
        widgets = {
                'foranea': forms.Select(attrs={'class': 'form-control'}),
                'cliente_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'producto_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'cantidad_producto_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'precio_venta_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'fecha_venta_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'metodo_pago_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'total_venta_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'sucursal_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'usuario_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'num_factura_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                }

