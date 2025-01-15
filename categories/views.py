from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from categories.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.

class CategoriesList(generic.ListView):
    template_name = 'Categories/CRUD/index.html'

    def get_queryset(self):
        return Categories.objects.all().order_by('id')
    
    context_object_name = "categories"

class CategoriesCreate(generic.CreateView):
    template_name = 'Categories/CRUD/add.html'
    model = Categories
    form_class = FormCategories
    success_url = reverse_lazy('categories:home_categories')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class CategoriesEdit(generic.UpdateView):
    template_name = 'Categories/CRUD/edit.html'
    model = Categories
    form_class = FormCategories
    success_url = reverse_lazy('categories:home_categories')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class CategoriesDelete(generic.DeleteView):
    template_name = 'Categories/CRUD/delete.html'
    model = Categories
    context_object_name = "categories"
    success_url = reverse_lazy('categories:home_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.products_set.exists()
        return context