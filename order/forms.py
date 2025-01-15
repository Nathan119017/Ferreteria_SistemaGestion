from django import forms
from .models import Order
from datetime import datetime, timedelta

class FormOrder(forms.ModelForm):
    class Meta:
        model = Order
        exclude = [''] 
        fields = ['num_order', 'nombre_empleado', 'fecha_de_pedido', 'metodo_de_pago', 'estado_pago', 'estado_pedido','cai' ,'total',]
        widgets = {
            'num_order': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '' }),
            'nombre_empleado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_de_pedido': forms.DateInput(attrs={'class': 'form-control', 'type':"date"}),
            'metodo_de_pago': forms.Select(attrs={'class': 'form-control'}),
            'estado_pago': forms.Select(attrs={'class': 'form-control'}),
            'estado_pedido': forms.Select(attrs={'class': 'form-control'}),
            'cai': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
        }
        
      # Hace que el campo num_factura sea no editable en el formulario
    def __init__(self, *args, **kwargs):
        super(FormOrder, self).__init__(*args, **kwargs)
        self.fields['num_order'].disabled = True

class FormOrderWithValidation(FormOrder):
    def clean_fecha_de_pedido(self):
        fecha_de_pedido = self.cleaned_data['fecha_de_pedido']
        fecha_actual = datetime.now().date()
        diferencia = fecha_de_pedido - fecha_actual

        if abs(diferencia.days) > 3:
            raise forms.ValidationError('La fecha del Pedido no puede ser más ni menos de tres días del día actual.')

        return fecha_de_pedido
    
    
    
    