from django.db import models
from django.core.validators import RegexValidator

from order.models import Order

class Order_History(models.Model):
    foranea = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)

    num_order_cambio = models.CharField(max_length=50)
    nombre_empleado_cambio = models.CharField(max_length=50)
    fecha_de_pedido_cambio = models.CharField(max_length=50)
    metodo_de_pago_cambio = models.CharField(max_length=50)
    estado_pago_cambio = models.CharField(max_length=50)
    estado_pedido_cambio = models.CharField(max_length=50)
    cai_cambio = models.CharField(max_length=50)
    total_cambio = models.CharField(max_length=50)

    Fecha_Hora = models.DateTimeField(auto_now_add=True)
    
        
    