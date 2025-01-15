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

class ProductsDetailList(generic.ListView):
    template_name = 'Product_Details/CRUD/index.html'
    def get_queryset(self):
        return ProductsDetail.objects.all().order_by('id')
    context_object_name = "productdetails"

class ProductsDetailCreate(generic.CreateView):
    template_name = 'Product_Details/CRUD/add.html'
    model = ProductsDetail
    form_class = FormProductDetail
    success_url = reverse_lazy('productsdetail:home_productsdetail')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        has_discount_promotion = form.cleaned_data['has_discount_promotion']
        if not has_discount_promotion:
            form.instance.discount_promotion = None  # Establece la fecha de vencimiento en None
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class ProductsDetailEdit(generic.UpdateView):
    template_name = 'Product_Details/CRUD/edit.html'
    model = ProductsDetail
    form_class = FormProductDetail
    success_url = reverse_lazy('productsdetail:home_productsdetail')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        has_discount_promotion = form.cleaned_data['has_discount_promotion']
        if not has_discount_promotion:
            form.instance.discount_promotion = None  # Establece la fecha de vencimiento en None
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class ProductsDetailDelete(generic.DeleteView):
    template_name = 'Product_Details/CRUD/delete.html'
    model = ProductsDetail
    context_object_name = "productdetails"
    success_url = reverse_lazy('productsdetail:home_productsdetail')