# Generated by Django 4.2.10 on 2024-04-14 05:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0003_alter_tax_tasa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='tasa',
            field=models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.RegexValidator(code='invalid_number', message='El numero ingresado no es válido, no se permite ningun caracter especial, solo numeros de 4 digitos Ej: 12.45.', regex='^[0-9]{2}\\.[0-9]{2}$')]),
        ),
    ]