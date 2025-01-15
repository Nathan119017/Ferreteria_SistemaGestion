from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from sale_history.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.


class Sale_HistoryList(generic.ListView):
    template_name = 'Sale_History/CRUD/index.html'
    def get_queryset(self):
        return Sale_History.objects.all().order_by('id')
    context_object_name = "venta_historial"

class Sale_HistoryCreate(generic.CreateView):
    template_name = 'Sale_History/CRUD/add.html'
    model = Sale_History
    form_class = FormSale_History
    success_url = reverse_lazy('sale_history:home_sale_history')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Sale_HistoryEdit(generic.UpdateView):
    template_name = 'Sale_History/CRUD/edit.html'
    model = Sale_History
    form_class = FormSale_History
    success_url = reverse_lazy('sale_history:home_sale_history')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Sale_HistoryDelete(generic.DeleteView):
    template_name = 'Sale_History/CRUD/delete.html'
    model = Sale_History
    context_object_name = "venta_historial"
    success_url = reverse_lazy('sale_history:home_sale_history')
