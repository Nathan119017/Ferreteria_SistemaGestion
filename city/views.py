from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class CityList(ListView):
    template_name = 'City/CRUD/index.html'  # Se ha cambiado 'Tax' por 'City'
    queryset = City.objects.all().order_by('id')  # Se ha cambiado 'Tax' por 'City'
    context_object_name = "ciudades"  # Se ha cambiado 'impuestos' por 'ciudades'

class CityCreate(CreateView):
    template_name = 'City/CRUD/add.html'  # Se ha cambiado 'Tax' por 'City'
    model = City  # Se ha cambiado 'Tax' por 'City'
    form_class = FormCity  # Se ha cambiado 'FormTax' por 'FormCity'
    success_url = reverse_lazy('city:home_city')  # Se ha cambiado 'tax:home_tax' por 'city:home_city'

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})

class CityEdit(UpdateView):
    template_name = 'City/CRUD/edit.html'  # Se ha cambiado 'Tax' por 'City'
    model = City  # Se ha cambiado 'Tax' por 'City'
    form_class = FormCity  # Se ha cambiado 'FormTax' por 'FormCity'
    success_url = reverse_lazy('city:home_city')  # Se ha cambiado 'tax:home_tax' por 'city:home_city'

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})

class CityDelete(DeleteView):
    template_name = 'City/CRUD/delete.html'  # Se ha cambiado 'Tax' por 'City'
    model = City  # Se ha cambiado 'Tax' por 'City'
    context_object_name = "ciudades"  # Se ha cambiado 'impuestos' por 'ciudades'
    success_url = reverse_lazy('city:home_city')  # Se ha cambiado 'tax:home_tax' por 'city:home_city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.branch_offices_set.exists()
        return context

