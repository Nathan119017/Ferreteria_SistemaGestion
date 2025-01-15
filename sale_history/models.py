from django.db import models
from django.core.validators import RegexValidator

from sale.models import Sale

class Sale_History(models.Model):
    foranea = models.ForeignKey(Sale, on_delete=models.CASCADE, default=1)
    
    cliente_cambio = models.CharField(max_length=50)
    producto_cambio = models.CharField(max_length=50)
    cantidad_producto_cambio = models.CharField(max_length=50)
    precio_venta_cambio = models.CharField(max_length=50)
    fecha_venta_cambio = models.CharField(max_length=50)
    metodo_pago_cambio = models.CharField(max_length=50)
    total_venta_cambio = models.CharField(max_length=50)
    sucursal_cambio = models.CharField(max_length=50)
    usuario_cambio = models.CharField(max_length=50)
    num_factura_cambio = models.CharField(max_length=50)

    Fecha_Hora = models.DateTimeField(auto_now_add=True)
    
        
    