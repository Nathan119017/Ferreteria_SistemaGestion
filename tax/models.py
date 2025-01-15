from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

regex_desc = [
    (r'^[a-zA-Z\s]+$', 'El campo no permite caracteres especiales ni numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_desc]

pattern_number= r'^[0-9]{2}\.[0-9]{2}$'

validatornum = RegexValidator(
    regex = pattern_number,
    message='El numero ingresado no es válido, no se permite ningun caracter especial, solo numeros de 4 digitos Ej: 12.45.',
    code='invalid_number'
)

class Tax(models.Model):
    nombre = models.CharField(max_length=50, validators=validatorsaddress)
    tasa = models.DecimalField(max_digits=15, decimal_places=2, validators=[validatornum])

    def __str__(self):
        return str(self.id)

# Define la señal post_save aquí para evitar importación circular
@receiver(post_save, sender=Tax)
def create_tax_history(sender, instance, created, **kwargs):
    from tax_history.models import Tax_History  # Importa aquí para evitar importación circular
    if created:
        nombre_cambio = f'{instance.nombre}'
        tasa_cambio = f'{instance.tasa}'
        Tax_History.objects.create(foranea=instance, nombre_cambio=nombre_cambio, tasa_cambio=tasa_cambio)
    else:
        nombre_cambio = f'{instance.nombre}'
        tasa_cambio = f'{instance.tasa}'
        Tax_History.objects.create(foranea=instance, nombre_cambio=nombre_cambio, tasa_cambio=tasa_cambio)


