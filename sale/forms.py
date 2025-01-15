from django import forms
from .models import Sale
from datetime import datetime, timedelta

class FormSale(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ['']  # Excluye el campo num_factura del formulario
        fields = ['cliente', 'producto', 'cantidad_producto', 'precio_venta', 'fecha_venta', 'metodo_pago', 'total_venta', 'sucursal', 'usuario', 'num_factura']
        widgets = {
                'cliente': forms.Select(attrs={'class': 'form-control'}), 
                'producto': forms.Select(attrs={'class': 'form-control'}), 
                'cantidad_producto': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
                'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
                'fecha_venta': forms.DateInput(attrs={'class': 'form-control', 'type':"date"}), 
                'metodo_pago': forms.Select(attrs={'class': 'form-control'}), 
                'total_venta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
                'sucursal': forms.Select(attrs={'class': 'form-control'}), 
                'usuario': forms.Select(attrs={'class': 'form-control'}), 
                'num_factura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                }
        
    def __init__(self, *args, **kwargs):
        super(FormSale, self).__init__(*args, **kwargs)
        self.fields['num_factura'].disabled = True  # Hace que el campo num_factura sea no editable en el formulario


