from django import forms
from .models import Order_History
from datetime import datetime, timedelta



class FormOrder_History(forms.ModelForm):
    class Meta:
        model = Order_History
        fields = ['foranea', 'num_order_cambio', 'nombre_empleado_cambio', 'fecha_de_pedido_cambio', 'metodo_de_pago_cambio', 'estado_pago_cambio', 'estado_pedido_cambio', 'cai_cambio', 'total_cambio']
        widgets = {
                'foranea': forms.Select(attrs={'class': 'form-control'}),

                'num_order_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'nombre_empleado_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'fecha_de_pedido_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'metodo_de_pago_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'estado_pago_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'estado_pedido_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'cai_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                'total_cambio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                }

