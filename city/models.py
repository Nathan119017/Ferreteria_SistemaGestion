from django.db import models
from django.core.validators import RegexValidator

regex_address = [
    (r'^[a-zA-Z\s]+$', 'El campo no permite caracteres especiales ni numeros, solo letras.'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_address]

pattern_number=r'^[0-9]{5}$'

validatornum = RegexValidator(
    regex = pattern_number,
    message='El numero ingresado no es válido, el codigo postal debe ser de 5 digitos y solo numeros.',
    code='invalid_number'
    
)

class City(models.Model):  # Cambio de Tax a City
    nombre_ciudad = models.CharField(max_length=50, validators = validatorsaddress)  # Cambio de nombre del campo
    codigo_postal = models.CharField(max_length=5, validators =[validatornum])  # Cambio de nombre del campo

    def __str__(self):
        return self.nombre_ciudad