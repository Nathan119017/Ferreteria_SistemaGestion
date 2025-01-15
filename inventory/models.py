from django.core.exceptions import ValidationError
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator

from products.models import Products
from branch_offices.models import Branch_Offices

class Inventory(models.Model):
    lote = models.CharField(max_length=50, default='')
    cantidadinventario = models.IntegerField(default=0)
    fecha_ingreso = models.DateField(null=True, blank=True)
    cantidadminima = models.IntegerField(default=0, verbose_name="Cantidad Mínima", validators=[MinValueValidator(0)])
    cantidadmaxima = models.IntegerField(default=0, verbose_name="Cantidad Máxima", validators=[MinValueValidator(0)])
    idproducto = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name="Producto")
    idsucursal = models.ForeignKey(Branch_Offices, on_delete=models.PROTECT, verbose_name="Sucursal")

    def __str__(self):
        return self.lote

    def clean(self):
        super().clean()
        if self.cantidadinventario < self.cantidadminima:
            raise ValidationError({'cantidadinventario': 'La cantidad de inventario no puede ser menor que la cantidad mínima.'})
        if self.cantidadinventario > self.cantidadmaxima:
            raise ValidationError({'cantidadinventario': 'La cantidad de inventario no puede ser mayor que la cantidad máxima.'})

