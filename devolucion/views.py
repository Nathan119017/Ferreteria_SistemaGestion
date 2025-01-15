from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class DevolucionList(ListView):
    template_name = 'Devolucion/CRUD/index.html'
    queryset = Devolucion.objects.all().order_by('id')
    context_object_name = "devoluciones"

class DevolucionCreate(CreateView):
    template_name = 'Devolucion/CRUD/add.html'
    model = Devolucion
    form_class = FormDevolucion
    success_url = reverse_lazy('devolucion:home_devolucion')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class DevolucionEdit(UpdateView):
    template_name = 'Devolucion/CRUD/edit.html'
    model = Devolucion
    form_class = FormDevolucion
    success_url = reverse_lazy('devolucion:home_devolucion')
    
    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class DevolucionDelete(DeleteView):
    template_name = 'Devolucion/CRUD/delete.html'
    model = Devolucion
    context_object_name = "devolucion"
    success_url = reverse_lazy('devolucion:home_devolucion')

    
