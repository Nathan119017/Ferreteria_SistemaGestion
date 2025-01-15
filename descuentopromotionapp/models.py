from decimal import Decimal
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

PROMOTIONDISCOUNT_CHOICES = (
    ('P', 'Promocion'),
    ('D', 'Descuento'),
    ('O', 'Otro'),
)

PROMOTIONDISCOUNT_VALUES = (
    (Decimal('0.0'), '0%'),
    (Decimal('0.10'), '10%'),
    (Decimal('0.15'), '15%'),
    (Decimal('0.20'), '20%'),
    (Decimal('0.25'), '25%'),
    (Decimal('0.30'), '30%'),
    (Decimal('0.35'), '35%'),
    (Decimal('0.40'), '40%'),
    (Decimal('0.45'), '45%'),
    (Decimal('0.50'), '50%'),
    (Decimal('0.60'), '60%'),
    (Decimal('0.70'), '70%'),
    (Decimal('0.75'), '75%'),
    (Decimal('0.80'), '80%'),
    (Decimal('0.90'), '90%'),
    (Decimal('0.95'), '95%'),
)

regex_name = [
    (r'^[a-zA-Z0-9\s]+$', 'El campo no permite caracteres especiales, solo letras y numeros'),
]
validatorsname = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_name]

class PromDisc(models.Model):
    nombrepromocion_descuento = models.CharField(max_length=50, validators=validatorsname)
    porcentaje = models.DecimalField(max_digits=4, decimal_places=2, choices=PROMOTIONDISCOUNT_VALUES)
    promocion_descuento = models.CharField(max_length=20, choices=PROMOTIONDISCOUNT_CHOICES)
    
    def __str__(self):
        return self.nombrepromocion_descuento
    