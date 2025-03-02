from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Persona
from .forms import PersonaForm

class PersonaListView(ListView):
    model = Persona
    template_name = 'persona/persona_list.html'
    context_object_name = 'personas'

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/persona_form.html'
    success_url = reverse_lazy('persona_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadir datos de provincias y ciudades al contexto
        context['provincias_data'] = {
            'ARG': [{'id': '1', 'nombre': 'Buenos Aires'}, {'id': '2', 'nombre': 'Córdoba'}, 
                   {'id': '3', 'nombre': 'Santa Fe'}, {'id': '4', 'nombre': 'Mendoza'}],
            'BRA': [{'id': '1', 'nombre': 'São Paulo'}, {'id': '2', 'nombre': 'Rio de Janeiro'}, 
                   {'id': '3', 'nombre': 'Minas Gerais'}]
        }
        context['ciudades_data'] = {
            'Buenos Aires': [{'id': '1', 'nombre': 'La Plata'}, {'id': '2', 'nombre': 'Mar del Plata'}, 
                           {'id': '3', 'nombre': 'Bahía Blanca'}],
            'Córdoba': [{'id': '1', 'nombre': 'Córdoba'}, {'id': '2', 'nombre': 'Río Cuarto'}, 
                       {'id': '3', 'nombre': 'Villa María'}]
        }
        return context

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/persona_form.html'
    success_url = reverse_lazy('persona_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadir datos de provincias y ciudades al contexto
        context['provincias_data'] = {
            'ARG': [{'id': '1', 'nombre': 'Buenos Aires'}, {'id': '2', 'nombre': 'Córdoba'}, 
                   {'id': '3', 'nombre': 'Santa Fe'}, {'id': '4', 'nombre': 'Mendoza'}],
            'BRA': [{'id': '1', 'nombre': 'São Paulo'}, {'id': '2', 'nombre': 'Rio de Janeiro'}, 
                   {'id': '3', 'nombre': 'Minas Gerais'}]
        }
        context['ciudades_data'] = {
            'Buenos Aires': [{'id': '1', 'nombre': 'La Plata'}, {'id': '2', 'nombre': 'Mar del Plata'}, 
                           {'id': '3', 'nombre': 'Bahía Blanca'}],
            'Córdoba': [{'id': '1', 'nombre': 'Córdoba Capital'}, {'id': '2', 'nombre': 'Río Cuarto'}, 
                       {'id': '3', 'nombre': 'Villa María'}]
        }
        return context


class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'persona/persona_confirm_delete.html'
    success_url = reverse_lazy('persona_list')