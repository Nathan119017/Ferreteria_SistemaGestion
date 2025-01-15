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


class UsersList(generic.ListView):
    template_name = 'Users/CRUD/index.html'
    def get_queryset(self):
        return Users.objects.all().order_by('id')
    context_object_name = "usuarios"

class UsersCreate(generic.CreateView):
    template_name = 'Users/CRUD/add.html'
    model = Users
    form_class = FormUsersWithValidation
    success_url = reverse_lazy('users:home_users')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class UsersEdit(generic.UpdateView):
    template_name = 'Users/CRUD/edit.html'
    model = Users
    form_class = FormUsersWithValidation
    success_url = reverse_lazy('users:home_users')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class UsersDelete(generic.DeleteView):
    template_name = 'Users/CRUD/delete.html'
    model = Users
    context_object_name = "usuarios"
    success_url = reverse_lazy('users:home_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.order_set.exists()
        context['tiene_venta'] = proveedor.sale_set.exists()
        return context