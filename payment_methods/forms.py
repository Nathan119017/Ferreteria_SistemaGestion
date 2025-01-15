from django import forms
from .models import *
from django.contrib.auth.models import User

class FormPayment_Methods(forms.ModelForm):

    class Meta:
        model = Payment_Methods
        fields = ['tipo_metodo_pago', 'descripcion']
        widgets = {
                'tipo_metodo_pago': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Codigo de Metodo de Pago. Ejem. CONT - (Contado)'}),
                'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Descripcion del tipo de pago. Ejem. Pago en Efectivo'  }),
                }
