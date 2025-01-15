from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from clients.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.

class ClientsList(generic.ListView):
    template_name = 'Clients/CRUD/index.html'

    def get_queryset(self):
        return Clients.objects.all().order_by('id')
    
    context_object_name = "clientes"

class ClientsCreate(generic.CreateView):
    template_name = 'Clients/CRUD/add.html'
    model = Clients
    form_class = FormClientsWithValidation
    success_url = reverse_lazy('clients:home_clients')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class ClientsEdit(generic.UpdateView):
    template_name = 'Clients/CRUD/edit.html'
    model = Clients
    form_class = FormClientsWithValidation
    success_url = reverse_lazy('clients:home_clients')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class ClientsDelete(generic.DeleteView):
    template_name = 'Clients/CRUD/delete.html'
    model = Clients
    context_object_name = "clientes"
    success_url = reverse_lazy('clients:home_clients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.sale_set.exists()
        return context