from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from tax_history.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.


class Tax_HistoryList(generic.ListView):
    template_name = 'Tax_History/CRUD/index.html'
    def get_queryset(self):
        return Tax_History.objects.all().order_by('id')
    context_object_name = "impuesto_historial"

class Tax_HistoryCreate(generic.CreateView):
    template_name = 'Tax_History/CRUD/add.html'
    model = Tax_History
    form_class = FormTax_History
    success_url = reverse_lazy('tax_history:home_tax_history')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Tax_HistoryEdit(generic.UpdateView):
    template_name = 'Tax_History/CRUD/edit.html'
    model = Tax_History
    form_class = FormTax_History
    success_url = reverse_lazy('tax_history:home_tax_history')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Tax_HistoryDelete(generic.DeleteView):
    template_name = 'Tax_History/CRUD/delete.html'
    model = Tax_History
    context_object_name = "impuesto_historial"
    success_url = reverse_lazy('tax_history:home_tax_history')
