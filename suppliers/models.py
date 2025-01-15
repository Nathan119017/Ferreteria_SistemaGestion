from django.db import models
from django.core.validators import RegexValidator

pattern_number= r'^[0-9]{8}$'

validatornum = RegexValidator(
    regex = pattern_number,
    message='El numero ingresado no es válido, el numero de telefono debe ser de 8 digitos y solo numeros.',
    code='invalid_number'
    
)


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

class Suppliers(models.Model):
    nombre = models.CharField(max_length=50, validators=validatorsname)
    apellido = models.CharField(max_length=50, validators=validatorslastname)
    nombre_de_empresa = models.CharField(max_length=50, validators=validatorsaddress )
    telefono = models.CharField(max_length=8, validators=[validatornum])
    direccion = models.CharField(max_length=50, validators=validatorsaddress)
    correo_electronico = models.EmailField(max_length = 100)
    
    def __str__(self):
        return self.nombre_de_empresa