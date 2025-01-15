from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

regex_address = [
    (r'^[a-zA-Z0-9\s]+$', 'El campo no permite caracteres especiales, solo letras y numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_address]

class Devolucion(models.Model):
    nombre_producto = models.CharField(max_length=50, validators = validatorsaddress)
    cantidad_retornada = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

# Define la señal post_save aquí para evitar importación circular
@receiver(post_save, sender=Devolucion)
def create_devolucion_history(sender, instance, created, **kwargs):
    from devolucion_history.models import Devolucion_History  # Importa aquí para evitar importación circular
    if created:
        nombre_producto_cambio = f'{instance.nombre_producto}'
        cantidad_retornada_cambio = f'{instance.cantidad_retornada}'
        Devolucion_History.objects.create(foranea=instance, nombre_producto_cambio=nombre_producto_cambio, cantidad_retornada_cambio=cantidad_retornada_cambio)
    else:
        nombre_producto_cambio = f'{instance.nombre_producto}'
        cantidad_retornada_cambio = f'{instance.cantidad_retornada}'
        Devolucion_History.objects.create(foranea=instance, nombre_producto_cambio=nombre_producto_cambio, cantidad_retornada_cambio=cantidad_retornada_cambio)