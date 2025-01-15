from django.db import models
from django.core.validators import RegexValidator
from suppliers.models import Suppliers

regex_address = [
    (r'^[a-zA-Z0-9\s]+$', 'El campo no permite caracteres especiales, solo letras y numeros'),
]
validatorsaddress = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_address]

regex_cai = [
    (r"^[0-9A-Z]{6}-[0-9A-Z]{6}-[0-9A-Z]{6}-[0-9A-Z]{6}-[0-9A-Z]{6}-[0-9A-Z]{2}$", 'CAI incorrecto ingrese uno utilizando el formato correcto. Ej.123456-ABCDEF-012345-ABCDEF-012345-AB'),
]
validatorcai = [RegexValidator(regex=pattern, message=message) for pattern, message in regex_cai]

class CAI(models.Model):
    nombre_empresa = models.ForeignKey(Suppliers, on_delete=models.PROTECT)
    cai = models.CharField(max_length=50, validators=validatorcai )

    def __str__(self):
        return str(self.nombre_empresa)