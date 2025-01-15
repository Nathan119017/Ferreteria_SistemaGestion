from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from suppliers.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.

class SuppliersList(generic.ListView):
    template_name = 'Suppliers/CRUD/index.html'
    def get_queryset(self):
        return Suppliers.objects.all().order_by('id')
    context_object_name = "proveedores"

class SuppliersCreate(generic.CreateView):
    template_name = 'Suppliers/CRUD/add.html'
    model = Suppliers
    form_class = FormSuppliers
    success_url = reverse_lazy('suppliers:home_suppliers')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class SuppliersEdit(generic.UpdateView):
    template_name = 'Suppliers/CRUD/edit.html'
    model = Suppliers
    form_class = FormSuppliers
    success_url = reverse_lazy('suppliers:home_suppliers')
    
    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class SuppliersDelete(generic.DeleteView):
    template_name = 'Suppliers/CRUD/delete.html'
    model = Suppliers
    context_object_name = "proveedores"
    success_url = reverse_lazy('suppliers:home_suppliers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.products_set.exists()
        context['tiene_cai'] = proveedor.cai_set.exists()
        return context