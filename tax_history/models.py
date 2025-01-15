from django.db import models
from django.core.validators import RegexValidator

from tax.models import Tax

class Tax_History(models.Model):
    foranea = models.ForeignKey(Tax, on_delete=models.CASCADE, default=1)
    nombre_cambio = models.CharField(max_length=50)
    tasa_cambio = models.CharField(max_length=50)
    Fecha_Hora = models.DateTimeField(auto_now_add=True)
    
        
    