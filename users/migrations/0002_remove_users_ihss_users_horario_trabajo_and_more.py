# Generated by Django 4.2.10 on 2024-04-13 04:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch_offices', '0002_branch_offices_ciudad_alter_branch_offices_direccion_and_more'),
        ('work_schedules', '0002_alter_work_schedules_dias_trabajo_and_more'),
        ('document_type', '0002_alter_document_type_descripcion_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='IHSS',
        ),
        migrations.AddField(
            model_name='users',
            name='horario_trabajo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='work_schedules.work_schedules'),
        ),
        migrations.AddField(
            model_name='users',
            name='sucursal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='branch_offices.branch_offices'),
        ),
        migrations.AddField(
            model_name='users',
            name='tipo_de_documento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='document_type.document_type'),
        ),
        migrations.AlterField(
            model_name='users',
            name='apellido',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='El campo no permite caracteres especiales ni numeros, solo letras', regex='^[a-zA-Z]+$'), django.core.validators.RegexValidator(message='La primera letra debe ser mayuscula, el campo no permite letras mayusculas luego de la primera letra', regex='^[A-Z][a-z]*$'), django.core.validators.RegexValidator(message='No se permite mas de una palabra en el campo.', regex='^[^\\s]+$'), django.core.validators.RegexValidator(message='El campo no permite tres mismas letras seguidas o mas.', regex='^(?:(?!(\\w)\\1\\1).)+$')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='direccion',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='El campo no permite caracteres especiales, solo letras y numeros', regex='^[a-zA-Z0-9\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='estado_civil',
            field=models.CharField(choices=[('Soltero/a', 'Soltero/a'), ('Casado/a', 'Casado/a'), ('Unión libre', 'Unión libre o unión de hecho'), ('Separado/a', 'Separado/a'), ('Divorciado/a', 'Divorciado/a'), ('Viudo/a', 'Viudo/a')], max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='fecha_de_contratatacion',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='fecha_de_nacimiento',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1),
        ),
        migrations.AlterField(
            model_name='users',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='El campo no permite caracteres especiales ni numeros, solo letras', regex='^[a-zA-Z]+$'), django.core.validators.RegexValidator(message='La primera letra debe ser mayuscula, el campo no permite letras mayusculas luego de la primera letra', regex='^[A-Z][a-z]*$'), django.core.validators.RegexValidator(message='No se permite mas de una palabra en el campo.', regex='^[^\\s]+$'), django.core.validators.RegexValidator(message='El campo no permite tres mismas letras seguidas o mas.', regex='^(?:(?!(\\w)\\1\\1).)+$')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='salario',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='telefono',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='invalid_number', message='El numero ingresado no es válido, el numero de telefono debe ser de 8 digitos y solo numeros.', regex='^[0-9]{8}$')]),
        ),
    ]
