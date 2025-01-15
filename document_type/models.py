from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
regex_desc = [
    (r'^[a-zA-Z\s]+$', 'El campo no permite caracteres especiales ni numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_desc]


class Document_Type(models.Model):
    nombre = models.CharField(max_length=50, validators=validatorsaddress)
    descripcion = models.CharField(max_length=50, validators=validatorsaddress)


    def __str__(self):
        return self.nombre