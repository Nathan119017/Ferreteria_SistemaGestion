# Generated by Django 4.2.10 on 2024-04-13 04:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='fecha_de_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='descripcion',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='El campo no permite caracteres especiales, solo letras y numeros', regex='^[a-zA-Z0-9\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='categories',
            name='fecha_de_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='El campo no permite caracteres especiales ni numeros, solo letras', regex='^[a-zA-Z]+$'), django.core.validators.RegexValidator(message='La primera letra debe ser mayuscula, el campo no permite letras mayusculas luego de la primera letra', regex='^[A-Z][a-z]*$'), django.core.validators.RegexValidator(message='No se permite mas de una palabra en el campo.', regex='^[^\\s]+$'), django.core.validators.RegexValidator(message='El campo no permite tres mismas letras seguidas o mas.', regex='^(?:(?!(\\w)\\1\\1).)+$')]),
        ),
    ]
