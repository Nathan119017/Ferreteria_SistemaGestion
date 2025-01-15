from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from users.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.


class OrderList(generic.ListView):
    template_name = 'Order/CRUD/index.html'
    def get_queryset(self):
        return Order.objects.all().order_by('id')
    context_object_name = "order"

class OrderCreate(generic.CreateView):
    template_name = 'Order/CRUD/add.html'
    model = Order
    form_class = FormOrderWithValidation
    success_url = reverse_lazy('order:home_order')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class OrderEdit(generic.UpdateView):
    template_name = 'Order/CRUD/edit.html'
    model = Order
    form_class = FormOrderWithValidation
    success_url = reverse_lazy('order:home_order')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class OrderDelete(generic.DeleteView):
    template_name = 'Order/CRUD/delete.html'
    model = Order
    context_object_name = "order"
    success_url = reverse_lazy('order:home_order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.orderdetail_set.exists()
        return context

# Create your views here.
