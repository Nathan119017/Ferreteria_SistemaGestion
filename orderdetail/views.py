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


class OrderDetailList(generic.ListView):
    template_name = 'Order_Detail/CRUD/index.html'
    def get_queryset(self):
        return OrderDetail.objects.all().order_by('id')
    context_object_name = "orderdetail"

class OrderDetailCreate(generic.CreateView):
    template_name = 'Order_Detail/CRUD/add.html'
    model = OrderDetail
    form_class = FormOrderDetail
    success_url = reverse_lazy('orderdetail:home_orderdetail')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class OrderDetailEdit(generic.UpdateView):
    template_name = 'Order_Detail/CRUD/edit.html'
    model = OrderDetail
    form_class = FormOrderDetail
    success_url = reverse_lazy('orderdetail:home_orderdetail')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class OrderDetailDelete(generic.DeleteView):
    template_name = 'Order_Detail/CRUD/delete.html'
    model = OrderDetail
    context_object_name = "orderdetail"
    success_url = reverse_lazy('orderdetail:home_orderdetail')

