from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.http import JsonResponse

class SaleList(ListView):
    template_name = 'Sale/CRUD/index.html'
    queryset = Sale.objects.all().order_by('id')
    context_object_name = "venta"

class SaleCreate(CreateView):
    template_name = 'Sale/CRUD/add.html'
    model = Sale
    form_class = FormSale
    success_url = reverse_lazy('sale:home_sale')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class SaleEdit(UpdateView):
    template_name = 'Sale/CRUD/edit.html'
    model = Sale
    form_class = FormSale
    success_url = reverse_lazy('sale:home_sale')
    
    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class SaleDelete(DeleteView):
    template_name = 'Sale/CRUD/delete.html'
    model = Sale
    context_object_name = "venta"
    success_url = reverse_lazy('sale:home_sale')

