from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from order_history.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.


class Order_HistoryList(generic.ListView):
    template_name = 'Order_History/CRUD/index.html'
    def get_queryset(self):
        return Order_History.objects.all().order_by('id')
    context_object_name = "orden_historial"

class Order_HistoryCreate(generic.CreateView):
    template_name = 'Order_History/CRUD/add.html'
    model = Order_History
    form_class = FormOrder_History
    success_url = reverse_lazy('order_history:home_order_history')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Order_HistoryEdit(generic.UpdateView):
    template_name = 'Order_History/CRUD/edit.html'
    model = Order_History
    form_class = FormOrder_History
    success_url = reverse_lazy('order_history:home_order_history')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Order_HistoryDelete(generic.DeleteView):
    template_name = 'Order_History/CRUD/delete.html'
    model = Order_History
    context_object_name = "orden_historial"
    success_url = reverse_lazy('order_history:home_order_history')
