from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from branch_offices.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.

class Branch_OfficesList(generic.ListView):
    template_name = 'Branch_Offices/CRUD/index.html'

    def get_queryset(self):
        return Branch_Offices.objects.all().order_by('id')
    
    context_object_name = "branch_offices"

class Branch_OfficesCreate(generic.CreateView):
    template_name = 'Branch_Offices/CRUD/add.html'
    model = Branch_Offices
    form_class = FormBranch_Offices
    success_url = reverse_lazy('branch_offices:home_branch_offices')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Branch_OfficesEdit(generic.UpdateView):
    template_name = 'Branch_Offices/CRUD/edit.html'
    model = Branch_Offices
    form_class = FormBranch_Offices
    success_url = reverse_lazy('branch_offices:home_branch_offices')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Branch_OfficesDelete(generic.DeleteView):
    template_name = 'Branch_Offices/CRUD/delete.html'
    model = Branch_Offices
    context_object_name = "branch_offices"
    success_url = reverse_lazy('branch_offices:home_branch_offices')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.users_set.exists()
        context['tiene_inventario'] = proveedor.inventory_set.exists()
        context['tiene_venta'] = proveedor.sale_set.exists()
        return context