# Generated by Django 4.2.10 on 2024-03-20 21:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_Offices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sucursal', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Por favor, introduce un número de teléfono válido.', regex='^[0-9]{8}$')])),
                ('direccion', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=100)),
            ],
        ),
    ]