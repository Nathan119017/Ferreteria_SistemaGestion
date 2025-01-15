from django import forms
from .models import *

class FormWork_Schedules(forms.ModelForm):

    class Meta:
        
        
        model = Work_Schedules
        fields = ['inicio_jornada', 'fin_jornada', 'dias_trabajo']
        widgets = {
            'inicio_jornada': forms.Select(choices=HOURS_CHOICES, attrs={'class': 'form-control'}),
            'fin_jornada': forms.Select(choices=HOURS_CHOICES, attrs={'class': 'form-control'}),
            'dias_trabajo': forms.SelectMultiple(choices=DAYS_CHOICES, attrs={'class': 'form-control'}),
        }
        

                
