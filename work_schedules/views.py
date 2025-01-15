from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from work_schedules.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.


class Work_SchedulesList(generic.ListView):
    template_name = 'Work_Schedules/CRUD/index.html'
    def get_queryset(self):
        return Work_Schedules.objects.all().order_by('id')
    context_object_name = "work_schedules"

class Work_SchedulesCreate(generic.CreateView):
    template_name = 'Work_Schedules/CRUD/add.html'
    model = Work_Schedules
    form_class = FormWork_Schedules
    success_url = reverse_lazy('work_schedules:home_work_schedules')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Work_SchedulesEdit(generic.UpdateView):
    template_name = 'Work_Schedules/CRUD/edit.html'
    model = Work_Schedules
    form_class = FormWork_Schedules
    success_url = reverse_lazy('work_schedules:home_work_schedules')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Work_SchedulesDelete(generic.DeleteView):
    template_name = 'Work_Schedules/CRUD/delete.html'
    model = Work_Schedules
    context_object_name = "work_schedules"
    success_url = reverse_lazy('work_schedules:home_work_schedules')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.users_set.exists()
        return context