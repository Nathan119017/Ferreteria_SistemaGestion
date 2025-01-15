from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from document_type.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.

class Document_TypeList(generic.ListView):
    template_name = 'Document_Type/CRUD/index.html'

    def get_queryset(self):
        return Document_Type.objects.all().order_by('id')
    
    context_object_name = "document_type"

class Document_TypeCreate(generic.CreateView):
    template_name = 'Document_Type/CRUD/add.html'
    model = Document_Type
    form_class = FormDocument_Type
    success_url = reverse_lazy('document_type:home_document_type')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Document_TypeEdit(generic.UpdateView):
    template_name = 'Document_Type/CRUD/edit.html'
    model = Document_Type
    form_class = FormDocument_Type
    success_url = reverse_lazy('document_type:home_document_type')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Document_TypeDelete(generic.DeleteView):
    template_name = 'Document_Type/CRUD/delete.html'
    model = Document_Type
    context_object_name = "document_type"
    success_url = reverse_lazy('document_type:home_document_type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.users_set.exists()
        return context