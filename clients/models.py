from django.db import models
from django.core.validators import RegexValidator

from payment_methods.models import Payment_Methods

# Create your models here.

regex_name = [
    (r'^[a-zA-Z]+$', 'El campo no permite caracteres especiales ni numeros, solo letras'),
    (r'^[A-Z][a-z]*$','La primera letra debe ser mayuscula, el campo no permite letras mayusculas luego de la primera letra'),
    (r'^[^\s]+$','No se permite mas de una palabra en el campo.'),
    (r'^(?:(?!(\w)\1\1).)+$', 'El campo no permite tres mismas letras seguidas o mas.')
]
validatorsname = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_name]

regex_lastname = [
    (r'^[a-zA-Z]+$', 'El campo no permite caracteres especiales ni numeros, solo letras'),
    (r'^[A-Z][a-z]*$','La primera letra debe ser mayuscula, el campo no permite letras mayusculas luego de la primera letra'),
    (r'^[^\s]+$','No se permite mas de una palabra en el campo.'),
    (r'^(?:(?!(\w)\1\1).)+$', 'El campo no permite tres mismas letras seguidas o mas.')
]
validatorslastname = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_lastname]

regex_address = [
    (r'^[a-zA-Z0-9\s]+$', 'El campo no permite caracteres especiales, solo letras y numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_address]

payment_methods = [(method.id, method.tipo_metodo_pago) for method in Payment_Methods.objects.all()]

class Clients(models.Model):
    nombre = models.CharField(max_length=50, validators=validatorsname)
    apellido = models.CharField(max_length=50, validators=validatorslastname)
    fecha_de_nacimiento = models.DateField(max_length=50)
    direccion = models.CharField(max_length=50, validators=validatorsaddress)
    correo_electronico = models.EmailField(max_length = 100)
    metodos_pago = models.ForeignKey(Payment_Methods, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido}"

    
