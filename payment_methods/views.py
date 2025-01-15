from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View, generic

from payment_methods.forms import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

#views.

class Payment_MethodsList(generic.ListView):
    template_name = 'Payment_Methods/CRUD/index.html'
    def get_queryset(self):
        return Payment_Methods.objects.all().order_by('id')
    context_object_name = "payment_methods"

class Payment_MethodsCreate(generic.CreateView):
    template_name = 'Payment_Methods/CRUD/add.html'
    model = Payment_Methods
    form_class = FormPayment_Methods
    success_url = reverse_lazy('payment_methods:home_payment_methods')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Payment_MethodsEdit(generic.UpdateView):
    template_name = 'Payment_Methods/CRUD/edit.html'
    model = Payment_Methods
    form_class = FormPayment_Methods
    success_url = reverse_lazy('payment_methods:home_payment_methods')
    
    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class Payment_MethodsDelete(generic.DeleteView):
    template_name = 'Payment_Methods/CRUD/delete.html'
    model = Payment_Methods
    context_object_name = "payment_methods"
    success_url = reverse_lazy('payment_methods:home_payment_methods')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.clients_set.exists()
        context['tiene_order'] = proveedor.order_set.exists()
        context['tiene_venta'] = proveedor.sale_set.exists()
        return context