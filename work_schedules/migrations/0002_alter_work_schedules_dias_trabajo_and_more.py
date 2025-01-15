# Generated by Django 4.2.10 on 2024-04-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_schedules',
            name='dias_trabajo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='work_schedules',
            name='duracion_jornada',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='work_schedules',
            name='fin_jornada',
            field=models.CharField(choices=[('1 AM', '1 AM'), ('2 AM', '2 AM'), ('3 AM', '3 AM'), ('4 AM', '4 AM'), ('5 AM', '5 AM'), ('6 AM', '6 AM'), ('7 AM', '7 AM'), ('8 AM', '8 AM'), ('9 AM', '9 AM'), ('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 AM', '12 AM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM'), ('8 PM', '8 PM'), ('9 PM', '9 PM'), ('10 PM', '10 PM'), ('11 PM', '11 PM'), ('12 PM', '12 PM')], max_length=20),
        ),
        migrations.AlterField(
            model_name='work_schedules',
            name='inicio_jornada',
            field=models.CharField(choices=[('1 AM', '1 AM'), ('2 AM', '2 AM'), ('3 AM', '3 AM'), ('4 AM', '4 AM'), ('5 AM', '5 AM'), ('6 AM', '6 AM'), ('7 AM', '7 AM'), ('8 AM', '8 AM'), ('9 AM', '9 AM'), ('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 AM', '12 AM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM'), ('8 PM', '8 PM'), ('9 PM', '9 PM'), ('10 PM', '10 PM'), ('11 PM', '11 PM'), ('12 PM', '12 PM')], max_length=20),
        ),
    ]
