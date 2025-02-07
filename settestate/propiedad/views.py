from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Propiedad, Atributo, ValorAtributo
from .forms import PropiedadForm, AtributoForm, ValorAtributoForm

# Vistas para Propiedad
class PropiedadListView(ListView):
    model = Propiedad
    template_name = 'propiedad/propiedad_list.html'
    context_object_name = 'propiedades'

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

# Vistas para Atributo
class AtributoCreateView(CreateView):
    model = Atributo
    form_class = AtributoForm
    template_name = 'propiedad/atributo_form.html'
    success_url = reverse_lazy('propiedad_list')

class AtributoDeleteView(DeleteView):
    model = Atributo
    template_name = 'propiedad/atributo_confirm_delete.html'
    success_url = reverse_lazy('propiedad_list')

# Vistas para ValorAtributo
class ValorAtributoCreateView(CreateView):
    model = ValorAtributo
    form_class = ValorAtributoForm
    template_name = 'propiedad/valoratributo_form.html'
    success_url = reverse_lazy('propiedad_list')

    def form_valid(self, form):
        form.instance.propiedad_id = self.kwargs['propiedad_id']
        return super().form_valid(form)

class ValorAtributoDeleteView(DeleteView):
    model = ValorAtributo
    template_name = 'propiedad/valoratributo_confirm_delete.html'
    success_url = reverse_lazy('propiedad_list')