from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class TaxList(ListView):
    template_name = 'Tax/CRUD/index.html'
    queryset = Tax.objects.all().order_by('id')
    context_object_name = "impuestos"

class TaxCreate(CreateView):
    template_name = 'Tax/CRUD/add.html'
    model = Tax
    form_class = FormTax
    success_url = reverse_lazy('tax:home_tax')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class TaxEdit(UpdateView):
    template_name = 'Tax/CRUD/edit.html'
    model = Tax
    form_class = FormTax
    success_url = reverse_lazy('tax:home_tax')
    
    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class TaxDelete(DeleteView):
    template_name = 'Tax/CRUD/delete.html'
    model = Tax
    context_object_name = "impuestos"
    success_url = reverse_lazy('tax:home_tax')

    
