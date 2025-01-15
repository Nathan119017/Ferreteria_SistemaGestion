# Generated by Django 4.2.10 on 2024-04-13 04:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='codigo_postal',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(code='invalid_number', message='El numero ingresado no es válido, el codigo postal debe ser de 5 digitos y solo numeros.', regex='^[0-9]{5}$')]),
        ),
        migrations.AlterField(
            model_name='city',
            name='nombre_ciudad',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='El campo no permite caracteres especiales ni numeros, solo letras.', regex='^[a-zA-Z\\s]+$')]),
        ),
    ]