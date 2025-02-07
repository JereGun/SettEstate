from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ImagenPropiedad
from .forms import ImagenPropiedadForm


# Vistas para ImagenPropiedad
class ImagenPropiedadCreateView(CreateView):
    model = ImagenPropiedad
    form_class = ImagenPropiedadForm
    template_name = 'propiedad/imagenpropiedad_form.html'
    success_url = reverse_lazy('propiedad_list')

    def form_valid(self, form):
        form.instance.propiedad_id = self.kwargs['propiedad_id']
        return super().form_valid(form)

class ImagenPropiedadDeleteView(DeleteView):
    model = ImagenPropiedad
    template_name = 'propiedad/imagenpropiedad_confirm_delete.html'
    success_url = reverse_lazy('propiedad_list')