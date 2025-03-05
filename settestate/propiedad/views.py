from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db import models
from .models import Propiedad
from .forms import PropiedadForm
from imagen.models import ImagenPropiedad

# Vistas para Propiedad
class PropiedadListView(ListView):
    model = Propiedad
    template_name = 'propiedad/propiedad_list.html'
    context_object_name = 'propiedades'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('dueño')
        search_query = self.request.GET.get('search', '')
        search_field = self.request.GET.get('field', 'all')

        if search_query:
            if search_field == 'nombre':
                queryset = queryset.filter(nombre__icontains=search_query)
            elif search_field == 'dueño':
                queryset = queryset.filter(
                    models.Q(dueño__nombre__icontains=search_query) |
                    models.Q(dueño__apellido__icontains=search_query) |
                    models.Q(dueño__documento__icontains=search_query)
                )
            else:
                queryset = queryset.filter(
                    models.Q(nombre__icontains=search_query) |
                    models.Q(dueño__nombre__icontains=search_query) |
                    models.Q(dueño__apellido__icontains=search_query) |
                    models.Q(dueño__documento__icontains=search_query)
                )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['search_field'] = self.request.GET.get('field', 'all')
        return context

class PropiedadCreateView(CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'propiedad/propiedad_form.html'
    success_url = reverse_lazy('propiedad_list')

class PropiedadUpdateView(UpdateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'propiedad/propiedad_form.html'
    success_url = reverse_lazy('propiedad_list')

class PropiedadDeleteView(DeleteView):
    model = Propiedad
    template_name = 'propiedad/propiedad_confirm_delete.html'
    success_url = reverse_lazy('propiedad_list')

class PropiedadDetailView(DetailView):
    model = Propiedad
    template_name = 'propiedad/propiedad_detail.html'

# Vistas para ImagenPropiedad

ImagenFormSet = inlineformset_factory(Propiedad, ImagenPropiedad, fields=('imagen',), extra=3)

def crear_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            propiedad = form.save()
            formset = ImagenFormSet(request.POST, request.FILES, instance=propiedad)
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Propiedad creada exitosamente.')
                return redirect('propiedad_list')
    else:
        form = PropiedadForm()
        formset = ImagenFormSet()
    
    return render(request, 'propiedad/propiedad_form.html', {
        'form': form,
        'formset': formset
    })

def editar_propiedad(request, pk):
    propiedad = Propiedad.objects.get(pk=pk)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            propiedad = form.save()
            formset = ImagenFormSet(request.POST, request.FILES, instance=propiedad)
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Propiedad actualizada exitosamente.')
                return redirect('propiedad_list')
    else:
        form = PropiedadForm(instance=propiedad)
        formset = ImagenFormSet(instance=propiedad)
    
    return render(request, 'propiedad/propiedad_form.html', {
        'form': form,
        'formset': formset
    })