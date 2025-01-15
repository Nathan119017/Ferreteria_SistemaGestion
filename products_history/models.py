from django.db import models
from django.core.validators import RegexValidator

from products.models import Products

class Products_History(models.Model):
    foranea = models.ForeignKey(Products, on_delete=models.CASCADE, default=1)
    
    nombre_cambio = models.CharField(max_length=50)
    descripcion_cambio = models.CharField(max_length=50)
    fecha_de_vencimiento_cambio = models.CharField(max_length=50)
    stock_cambio = models.CharField(max_length=50)
    precio_cambio = models.CharField(max_length=50)
    categoria_cambio = models.CharField(max_length=50)
    proveedor_cambio = models.CharField(max_length=50)

    Fecha_Hora = models.DateTimeField(auto_now_add=True)
    
        
    