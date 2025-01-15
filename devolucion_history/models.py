from django.db import models
from django.core.validators import RegexValidator

from devolucion.models import Devolucion

class Devolucion_History(models.Model):
    foranea = models.ForeignKey(Devolucion, on_delete=models.CASCADE, default=1)
    nombre_producto_cambio = models.CharField(max_length=50)
    cantidad_retornada_cambio = models.CharField(max_length=50)
    Fecha_Hora = models.DateTimeField(auto_now_add=True)
    
        
    