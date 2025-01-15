# Generated by Django 4.2.10 on 2024-03-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work_Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_jornada', models.CharField(choices=[(1, '1 AM'), (2, '2 AM'), (3, '3 AM'), (4, '4 AM'), (5, '5 AM'), (6, '6 AM'), (7, '7 AM'), (8, '8 AM'), (9, '9 AM'), (10, '10 AM'), (11, '11 AM'), (12, '12 AM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM'), (18, '6 PM'), (19, '7 PM'), (20, '8 PM'), (21, '9 PM'), (22, '10 PM'), (23, '11 PM'), (24, '12 PM')], max_length=20)),
                ('fin_jornada', models.CharField(choices=[(1, '1 AM'), (2, '2 AM'), (3, '3 AM'), (4, '4 AM'), (5, '5 AM'), (6, '6 AM'), (7, '7 AM'), (8, '8 AM'), (9, '9 AM'), (10, '10 AM'), (11, '11 AM'), (12, '12 AM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM'), (18, '6 PM'), (19, '7 PM'), (20, '8 PM'), (21, '9 PM'), (22, '10 PM'), (23, '11 PM'), (24, '12 PM')], max_length=20)),
                ('dias_trabajo', models.CharField(choices=[(1, '1 AM'), (2, '2 AM'), (3, '3 AM'), (4, '4 AM'), (5, '5 AM'), (6, '6 AM'), (7, '7 AM'), (8, '8 AM'), (9, '9 AM'), (10, '10 AM'), (11, '11 AM'), (12, '12 AM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM'), (18, '6 PM'), (19, '7 PM'), (20, '8 PM'), (21, '9 PM'), (22, '10 PM'), (23, '11 PM'), (24, '12 PM')], max_length=20)),
                ('duracion_jornada', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('tipo_jornada', models.CharField(choices=[('Matutina', 'Jornada Matutina'), ('Vespertina', 'Jornada Vespertina'), ('Nocturna', 'Jornada Nocturna')], max_length=20)),
            ],
        ),
    ]
