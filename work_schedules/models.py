from django.db import models
from django.core.exceptions import ValidationError

HOURS_CHOICES = [(f'{hour} AM', f'{hour} AM') for hour in range(1, 13)] + \
                [(f'{hour} PM', f'{hour} PM') for hour in range(1, 13)]

DAYS_CHOICES = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sabado', 'Sábado'),
    ('Domingo', 'Domingo')
]

JORNADA_CHOICES = [
    ('Matutina', 'Jornada Matutina'),
    ('Vespertina', 'Jornada Vespertina'),
    ('Nocturna', 'Jornada Nocturna'),
]


class Work_Schedules(models.Model):
    inicio_jornada = models.CharField(max_length=20, choices=HOURS_CHOICES)
    fin_jornada = models.CharField(max_length=20, choices=HOURS_CHOICES)
    dias_trabajo = models.CharField(max_length=150)
    duracion_jornada = models.CharField(max_length=10)
    tipo_jornada = models.CharField(max_length=20, choices=JORNADA_CHOICES)


    def __str__(self):
        return f'{self.id}'
    
    def save(self, *args, **kwargs):
        if self.inicio_jornada and self.fin_jornada:
            inicio_hour, inicio_period = self.inicio_jornada.split()
            fin_hour, fin_period = self.fin_jornada.split()

            inicio_hour = int(inicio_hour) + (12 if inicio_period == 'PM' else 0)
            fin_hour = int(fin_hour) + (12 if fin_period == 'PM' else 0)

            duracion = fin_hour - inicio_hour
            if duracion < 0:
                duracion += 24

            self.duracion_jornada = f'{duracion} Horas'

            if inicio_hour < 12:
                self.tipo_jornada = 'Matutina'
            elif inicio_hour < 18:
                self.tipo_jornada = 'Vespertina'
            else:
                self.tipo_jornada = 'Nocturna'

        else:
            raise ValidationError('Debe establecer tanto el inicio como el fin de la jornada.')

        super().save(*args, **kwargs)

        
