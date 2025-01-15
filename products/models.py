from django.db import models

from suppliers.models import Suppliers
from categories.models import Categories

# Create your models here.


class Products(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_de_vencimiento = models.DateField(max_length=50, null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    categoria = models.ForeignKey(Categories, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Suppliers, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre