from django.db import models
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.validators import RegexValidator

from document_type.models import Document_Type
from branch_offices.models import Branch_Offices
from work_schedules.models import Work_Schedules
from users.models import Users
from payment_methods.models import Payment_Methods
from cai.models import CAI


# Create your models here.
ORDER_CHOICES = (
    ('EP', 'En Proceso'),
    ('ENT', 'Entregado'),
    ('PRODFALT', 'Productos Faltantes'),
    ('B', 'Bueno'),
    ('R', 'Recibido'),
)

ESTADOSPAGO_CHOICES = (
    ('A', 'Aceptado'),
    ('D', 'Denegado'),
    ('P', 'Pendiente'),
)

class Order(models.Model):
    num_order = models.CharField(max_length=20, blank=True)
    nombre_empleado = models.ForeignKey(Users, on_delete=models.PROTECT)
    fecha_de_pedido = models.DateField(max_length=50)
    metodo_de_pago = models.ForeignKey(Payment_Methods, on_delete=models.PROTECT)
    estado_pago = models.CharField(max_length=20, choices=ESTADOSPAGO_CHOICES)
    estado_pedido = models.CharField(max_length=20, choices=ORDER_CHOICES)
    cai= models.ForeignKey(CAI, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.num_order
    
    def save(self, *args, **kwargs):
        if not self.num_order:
            self.num_order = generate_invoice_code(sender=None, instance=self)
        super().save(*args, **kwargs)

@receiver(pre_save, sender=Order)
def generate_invoice_code(sender, instance, **kwargs):
    if not instance.num_order:
        # Lógica para generar el código de factura
        # Aquí puedes generar un código único, por ejemplo:
        last_sale = Order.objects.order_by('-id').first()
        if last_sale:
            last_code = last_sale.num_order.split('-')[-1]
            new_code = int(last_code) + 1
            instance.num_order = f'ORDER-{new_code:05d}'
        else:
            instance.num_order = 'ORDER-00001'

@receiver(post_save, sender=Order)
def create_order_history(sender, instance, created, **kwargs):
    from order_history.models import Order_History  # Importa aquí para evitar importación circular
    if created:
        num_order_cambio = f'{instance.num_order}'
        nombre_empleado_cambio = f'{instance.nombre_empleado}'
        fecha_de_pedido_cambio = f'{instance.fecha_de_pedido}'
        metodo_de_pago_cambio = f'{instance.metodo_de_pago}'
        estado_pago_cambio = f'{instance.estado_pago}'
        estado_pedido_cambio = f'{instance.estado_pedido}'
        cai_cambio = f'{instance.cai}'
        total_cambio = f'{instance.total}'
        Order_History.objects.create(foranea=instance, num_order_cambio=num_order_cambio, nombre_empleado_cambio=nombre_empleado_cambio, fecha_de_pedido_cambio=fecha_de_pedido_cambio, metodo_de_pago_cambio=metodo_de_pago_cambio, estado_pago_cambio=estado_pago_cambio, estado_pedido_cambio=estado_pedido_cambio, cai_cambio=cai_cambio, total_cambio=total_cambio)
    else:
        num_order_cambio = f'{instance.num_order}'
        nombre_empleado_cambio = f'{instance.nombre_empleado}'
        fecha_de_pedido_cambio = f'{instance.fecha_de_pedido}'
        metodo_de_pago_cambio = f'{instance.metodo_de_pago}'
        estado_pago_cambio = f'{instance.estado_pago}'
        estado_pedido_cambio = f'{instance.estado_pedido}'
        cai_cambio = f'{instance.cai}'
        total_cambio = f'{instance.total}'
        Order_History.objects.create(foranea=instance, num_order_cambio=num_order_cambio, nombre_empleado_cambio=nombre_empleado_cambio, fecha_de_pedido_cambio=fecha_de_pedido_cambio, metodo_de_pago_cambio=metodo_de_pago_cambio, estado_pago_cambio=estado_pago_cambio, estado_pedido_cambio=estado_pedido_cambio, cai_cambio=cai_cambio, total_cambio=total_cambio)
        
