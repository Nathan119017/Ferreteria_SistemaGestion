from django.db import models
from django.core.validators import RegexValidator

from city.models import City
# Create your models here.

regex_address = [
    (r'^[a-zA-Z0-9\s]+$', 'El campo no permite caracteres especiales, solo letras y numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_address]

class Branch_Offices(models.Model):
    nombre_sucursal = models.CharField(max_length=50, validators=validatorsaddress)
    telefono = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$', message='Por favor, introduce un número de teléfono válido.')])
    direccion = models.CharField(max_length=50, validators=validatorsaddress)
    correo_electronico = models.EmailField(max_length = 100)
    ciudad = models.ForeignKey(City, on_delete=models.PROTECT, default= 1 )

    def __str__(self):
        return self.nombre_sucursal