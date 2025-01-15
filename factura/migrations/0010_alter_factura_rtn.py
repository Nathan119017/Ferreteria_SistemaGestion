# Generated by Django 4.2.10 on 2024-04-28 22:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0009_factura_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='RTN',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='El requiere 14 digitos no letras ni caracteres especiales', regex='^\\d{14}$')]),
        ),
    ]
