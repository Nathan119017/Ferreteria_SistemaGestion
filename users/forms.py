from django import forms
from .models import Users
from datetime import datetime, timedelta

class FormUsers(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['nombre', 'apellido', 'direccion', 'fecha_de_nacimiento', 'telefono', 'fecha_de_contratatacion', 'genero', 'salario', 'tipo_de_documento', 'estado_civil', 'sucursal', 'horario_trabajo']
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre. Ejem. Mario Luis' }),
                'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Apellido. Ejem. Aguirre Gutierrez' }),
                'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la direccion de casa, Ejem. C. Mario Jaar, Tegucigalpa, Francisco Morazán'}), 
                'fecha_de_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type':"date"}),
                'telefono': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese el Numero de Telefono. Ejem. 12345678'}), 
                'fecha_de_contratatacion': forms.DateInput(attrs={'class': 'form-control', 'type':"date"}),
                'genero': forms.Select(attrs={'class': 'form-control'}), 
                'salario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                'tipo_de_documento': forms.Select(attrs={'class': 'form-control'}), 
                'sucursal': forms.Select(attrs={'class': 'form-control'}),   
                'estado_civil': forms.Select(attrs={'class': 'form-control'}),
                'horario_trabajo': forms.Select(attrs={'class': 'form-control'}), 
                }

class FormUsersWithValidation(FormUsers):
    def clean_fecha_de_contratatacion(self):
        fecha_de_contratatacion = self.cleaned_data['fecha_de_contratatacion']
        fecha_actual = datetime.now().date()
        diferencia = fecha_de_contratatacion - fecha_actual

        if abs(diferencia.days) > 3:
            raise forms.ValidationError('La fecha de contratación no puede ser más ni menos de tres días del día actual.')

        return fecha_de_contratatacion
    
    
    def clean_fecha_de_nacimiento(self):
        fecha_de_nacimiento = self.cleaned_data['fecha_de_nacimiento']
        edad_minima = datetime.now().date() - timedelta(days=18 * 365)  # Se resta la edad mínima de 18 años en días
        if fecha_de_nacimiento > edad_minima:
            raise forms.ValidationError('El empleado debe tener al menos 18 años de edad.')
        return fecha_de_nacimiento
                
