from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.core.validators import RegexValidator

from products.models import Products
from order.models import Order
from payment_methods.models import Payment_Methods


# Create your models here.
regex_address = [
    (r'^[a-zA-Z0-9\s]+$', 'El campo no permite caracteres especiales, solo letras y numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_address]


class OrderDetail(models.Model):
    num_order = models.ForeignKey(Order, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    nombre_product = models.ForeignKey(Products, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=200, validators= validatorsaddress)
    precio_unitario = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    