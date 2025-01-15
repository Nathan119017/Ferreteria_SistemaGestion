from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from users.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib import messages

#views.


class InventoryList(generic.ListView):
    template_name = 'Inventory/CRUD/index.html'
    def get_queryset(self):
        return Inventory.objects.all().order_by('id')
    context_object_name = "inventario"

class InventoryCreate(generic.CreateView):
    template_name = 'Inventory/CRUD/add.html'
    model = Inventory
    form_class = FormInventory
    success_url = reverse_lazy('inventory:home_inventory')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class InventoryEdit(generic.UpdateView):
    template_name = 'Inventory/CRUD/edit.html'
    model = Inventory
    form_class = FormInventory
    success_url = reverse_lazy('inventory:home_inventory')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class InventoryDelete(generic.DeleteView):
    template_name = 'Inventory/CRUD/delete.html'
    model = Inventory
    context_object_name = "inventario"
    success_url = reverse_lazy('inventory:home_inventory')

    
    