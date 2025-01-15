from django.shortcuts import render
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


class DiscPromList(generic.ListView):
    template_name = 'Prom_Disc/CRUD/index.html'
    def get_queryset(self):
        return PromDisc.objects.all().order_by('id')
    context_object_name = "discprom"

class DiscPromCreate(generic.CreateView):
    template_name = 'Prom_Disc/CRUD/add.html'
    model = PromDisc
    form_class = FormDiscP
    success_url = reverse_lazy('discprom:home_discprom')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class DiscPromEdit(generic.UpdateView):
    template_name = 'Prom_Disc/CRUD/edit.html'
    model = PromDisc
    form_class = FormDiscP
    success_url = reverse_lazy('discprom:home_discprom')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class DiscPromDelete(generic.DeleteView):
    template_name = 'Prom_Disc/CRUD/delete.html'
    model = PromDisc
    context_object_name = "discprom"
    success_url = reverse_lazy('discprom:home_discprom')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.productsdetail_set.exists()
        return context
