from django import forms
from .models import *
from django.contrib.auth.models import User

class FormInventory(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['lote', 'cantidadinventario', 'fecha_ingreso', 'cantidadminima', 'cantidadmaxima', 'idproducto', 'idsucursal' ]
        widgets = {
            'lote': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código de lote'}),
            'cantidadinventario': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'placeholder': 'Ingrese la cantidad de inventario'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Seleccione la fecha de ingreso'}),
            'idproducto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el producto'}),
            'idsucursal': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione la sucursal'}),
        }

    def clean_lote(self):
        lote = self.cleaned_data.get('lote')
        if Inventory.objects.filter(lote=lote).exists():
            raise forms.ValidationError("El código de lote ya está en uso. Por favor, ingrese un código de lote único.")
        return lote

    def clean(self):
        cleaned_data = super().clean()
        cantidad_minima = cleaned_data.get("cantidadminima")
        cantidad_maxima = cleaned_data.get("cantidadmaxima")

        if cantidad_minima >= cantidad_maxima:
            raise forms.ValidationError("La cantidad mínima debe ser menor que la cantidad máxima.")
