from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.db.models.signals import post_save
from django.dispatch import receiver

from clients.models import Clients
from products.models import Products
from payment_methods.models import Payment_Methods
from users.models import Users
from branch_offices.models import Branch_Offices


# Create your models here.



class Sale(models.Model):
    cliente = models.ForeignKey(Clients, on_delete=models.PROTECT, default=None)
    producto = models.ForeignKey(Products, on_delete=models.PROTECT, default=None)
    cantidad_producto = models.IntegerField(default=0)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    fecha_venta = models.DateField(max_length=50)
    metodo_pago = models.ForeignKey(Payment_Methods, on_delete=models.PROTECT, default=None)
    total_venta = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    sucursal = models.ForeignKey(Branch_Offices, on_delete=models.PROTECT, default=None)
    usuario = models.ForeignKey(Users, on_delete=models.PROTECT, default=None)
    num_factura = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.num_factura:
            self.num_factura = generate_invoice_code(sender=None, instance=self)
        super().save(*args, **kwargs)

@receiver(pre_save, sender=Sale)
def generate_invoice_code(sender, instance, **kwargs):
    if not instance.num_factura:
        # Lógica para generar el código de factura
        # Aquí puedes generar un código único, por ejemplo:
        last_sale = Sale.objects.order_by('-id').first()
        if last_sale:
            last_code = last_sale.num_factura.split('-')[-1]
            new_code = int(last_code) + 1
            instance.num_factura = f'FACT-{new_code:05d}'
        else:
            instance.num_factura = 'FACT-00001'


# Define la señal post_save aquí para evitar importación circular
@receiver(post_save, sender=Sale)
def create_sale_history(sender, instance, created, **kwargs):
    from sale_history.models import Sale_History  # Importa aquí para evitar importación circular
    if created:
        cliente_cambio = f'{instance.cliente}'
        producto_cambio = f'{instance.producto}'
        cantidad_producto_cambio = f'{instance.cantidad_producto}'
        precio_venta_cambio = f'{instance.precio_venta}'
        fecha_venta_cambio = f'{instance.fecha_venta}'
        metodo_pago_cambio = f'{instance.metodo_pago}'
        total_venta_cambio = f'{instance.total_venta}'
        sucursal_cambio = f'{instance.sucursal}'
        usuario_cambio = f'{instance.usuario}'
        num_factura_cambio = f'{instance.num_factura}'
        Sale_History.objects.create(foranea=instance, cliente_cambio=cliente_cambio, producto_cambio=producto_cambio, cantidad_producto_cambio=cantidad_producto_cambio, precio_venta_cambio=precio_venta_cambio, fecha_venta_cambio=fecha_venta_cambio, metodo_pago_cambio=metodo_pago_cambio, total_venta_cambio=total_venta_cambio, sucursal_cambio=sucursal_cambio, usuario_cambio=usuario_cambio, num_factura_cambio=num_factura_cambio)
    else:
        cliente_cambio = f'{instance.cliente}'
        producto_cambio = f'{instance.producto}'
        cantidad_producto_cambio = f'{instance.cantidad_producto}'
        precio_venta_cambio = f'{instance.precio_venta}'
        fecha_venta_cambio = f'{instance.fecha_venta}'
        metodo_pago_cambio = f'{instance.metodo_pago}'
        total_venta_cambio = f'{instance.total_venta}'
        sucursal_cambio = f'{instance.sucursal}'
        usuario_cambio = f'{instance.usuario}'
        num_factura_cambio = f'{instance.num_factura}'
        Sale_History.objects.create(foranea=instance, cliente_cambio=cliente_cambio, producto_cambio=producto_cambio, cantidad_producto_cambio=cantidad_producto_cambio, precio_venta_cambio=precio_venta_cambio, fecha_venta_cambio=fecha_venta_cambio, metodo_pago_cambio=metodo_pago_cambio, total_venta_cambio=total_venta_cambio, sucursal_cambio=sucursal_cambio, usuario_cambio=usuario_cambio, num_factura_cambio=num_factura_cambio)

    
