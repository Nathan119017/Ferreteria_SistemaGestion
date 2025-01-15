from django.db import models
from descuentopromotionapp.models import PromDisc
from products.models import Products
from django.core.validators import RegexValidator

# Create your models here.
regex_address = [
    (r'^[a-zA-Z0-9\s]+$', 'El campo no permite caracteres especiales, solo letras y numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_address]


class ProductsDetail(models.Model):
    nombre = models.ForeignKey(Products, unique = False, on_delete=models.PROTECT)
    nombrepromocion_descuento = models.ForeignKey(PromDisc , null=True, blank=True, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    descripcion = models.CharField(max_length=200, validators= validatorsaddress)
    precio_final = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.nombre}"
    
    