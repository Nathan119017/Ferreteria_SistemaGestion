# Generated by Django 4.2.10 on 2024-04-28 22:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0010_alter_factura_rtn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='RTN',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message='El requiere 14 digitos no letras ni caracteres especiales', regex='^\\d{14}$')]),
        ),
    ]
