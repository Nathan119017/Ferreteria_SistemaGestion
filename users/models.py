from django.db import models

from django.core.validators import RegexValidator

from document_type.models import Document_Type
from branch_offices.models import Branch_Offices
from work_schedules.models import Work_Schedules


# Create your models here.
GENDER_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
)

ESTADOSCIVILES_CHOICES = (
    ('Soltero/a', 'Soltero/a'),
    ('Casado/a', 'Casado/a'),
    ('Unión libre', 'Unión libre o unión de hecho'),
    ('Separado/a', 'Separado/a'),
    ('Divorciado/a', 'Divorciado/a'),
    ('Viudo/a', 'Viudo/a'),
)

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


class Users(models.Model):
    nombre = models.CharField(max_length=50, validators=validatorsname)
    apellido = models.CharField(max_length=50, validators=validatorslastname )
    direccion = models.CharField(max_length=50, validators=validatorsaddress)
    fecha_de_nacimiento = models.DateField(max_length=50)
    telefono = models.CharField(max_length=8, validators=[validatornum])
    fecha_de_contratatacion = models.DateField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    salario = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    tipo_de_documento = models.ForeignKey(Document_Type, on_delete=models.PROTECT, default=1)
    sucursal = models.ForeignKey(Branch_Offices, on_delete=models.PROTECT, default=1)
    estado_civil = models.CharField(max_length=20, choices=ESTADOSCIVILES_CHOICES)
    horario_trabajo = models.ForeignKey(Work_Schedules, on_delete=models.PROTECT, default = 1)

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido} "



    
