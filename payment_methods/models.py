from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
regex_pay = [
    (r'^[A-Z]+$', 'El campo no permite caracteres especiales ni numeros, solo letras mayusculas'),
]
validatorsmayus = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_pay]

regex_desc = [
    (r'^[a-zA-Z\s]+$', 'El campo no permite caracteres especiales ni numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_desc]

class Payment_Methods(models.Model):
    tipo_metodo_pago = models.CharField(max_length=50, validators=validatorsmayus)
    descripcion = models.CharField(max_length=50, validators=validatorsaddress )
    
    def __str__(self):
        return self.tipo_metodo_pago