from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class CAIList(ListView):
    template_name = 'CAI/CRUD/index.html'
    queryset = CAI.objects.all().order_by('id')
    context_object_name = "cai"

class CAICreate(CreateView):
    template_name = 'CAI/CRUD/add.html'
    model = CAI
    form_class = FormCAI
    success_url = reverse_lazy('cai:home_cai')

    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class CAIEdit(UpdateView):
    template_name = 'CAI/CRUD/edit.html'
    model = CAI
    form_class = FormCAI
    success_url = reverse_lazy('cai:home_cai')
    
    def form_valid(self, form):
        # Aquí puedes hacer cualquier procesamiento adicional antes de guardar el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario no es válido, renderizamos la plantilla con el formulario y los errores
        return render(self.request, self.template_name, {'form': form})
    
class CAIDelete(DeleteView):
    template_name = 'CAI/CRUD/delete.html'
    model = CAI
    context_object_name = "cai"
    success_url = reverse_lazy('cai:home_cai')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedor = self.get_object()
        context['tiene_productos'] = proveedor.order_set.exists()
        return context
