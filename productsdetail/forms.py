from django import forms
from .models import *
from django.contrib.auth.models import User

class FormProductDetail(forms.ModelForm):
    has_discount_promotion = forms.BooleanField(required=False, label='¿Tiene descuento o promocion?')
    discount_promotion = forms.Select(attrs={'class': 'form-control'})


    class Meta:
        model = ProductsDetail
        fields = ['nombre', 'descripcion', 'nombrepromocion_descuento', 'cantidad', 'precio_unitario', 'descripcion','precio_final']
        widgets = {
                'nombre': forms.Select(attrs={'class': 'form-control'}),
                'nombrepromocion_descuento': forms.Select(attrs={'class': 'form-control'}),
                'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
                'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
                'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Descripcion del producto.'  }),
                'precio_final': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
                }
        
        def clean(self):
            cleaned_data = super().clean()
            has_discount_promotion = cleaned_data.get('has_discount_promotion')
            discount_promotion = cleaned_data.get('discount_promotion')

            if not has_discount_promotion and discount_promotion:
             raise forms.ValidationError('No puede especificar un descuento si no ha marcado la casilla correspondiente.')

            return cleaned_data