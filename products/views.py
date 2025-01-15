from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from products.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.

class ProductsList(generic.ListView):
    template_name = 'Products/CRUD/index.html'
    def get_queryset(self):
        return Products.objects.all().order_by('id')
    context_object_name = "productos"

class ProductsCreate(generic.CreateView):
    template_name = 'Products/CRUD/add.html'
    model = Products
    form_class = FormProducts
    success_url = reverse_lazy('products:home_products')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        has_expiry_date = form.cleaned_data['has_expiry_date']
        if not has_expiry_date:
            form.instance.fecha_de_vencimiento = None  # Establece la fecha de vencimiento en None
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class ProductsEdit(generic.UpdateView):
    template_name = 'Products/CRUD/edit.html'
    model = Products
    form_class = FormProducts
    success_url = reverse_lazy('products:home_products')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        has_expiry_date = form.cleaned_data['has_expiry_date']
        if not has_expiry_date:
            form.instance.fecha_de_vencimiento = None  # Establece la fecha de vencimiento en None
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class ProductsDelete(generic.DeleteView):
    template_name = 'Products/CRUD/delete.html'
    model = Products
    context_object_name = "productos"
    success_url = reverse_lazy('products:home_products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.inventory_set.exists()
        context['tiene_detalleproducto'] = proveedor.productsdetail_set.exists()
        context['tiene_venta'] = proveedor.sale_set.exists()
        return context

    