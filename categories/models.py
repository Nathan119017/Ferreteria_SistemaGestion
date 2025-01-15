from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
regex_name = [
    (r'^[a-zA-Z]+$', 'El campo no permite caracteres especiales ni numeros, solo letras'),
    (r'^[A-Z][a-z]*$','La primera letra debe ser mayuscula, el campo no permite letras mayusculas luego de la primera letra'),
    (r'^[^\s]+$','No se permite mas de una palabra en el campo.'),
    (r'^(?:(?!(\w)\1\1).)+$', 'El campo no permite tres mismas letras seguidas o mas.')
]
validatorsname = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_name]

regex_address = [
    (r'^[a-zA-Z0-9\s]+$', 'El campo no permite caracteres especiales, solo letras y numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_address]

class Categories(models.Model):
    nombre = models.CharField(max_length=50, validators=validatorsname)
    descripcion = models.CharField(max_length=50, validators=validatorsaddress)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre