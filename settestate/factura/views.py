from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Factura, ItemFactura
from .forms import FacturaForm, ItemFacturaForm


class FacturaCreateView(LoginRequiredMixin, CreateView):
    model = Factura
    form_class = FacturaForm  # Usa form_class en lugar de fields
    template_name = 'factura/factura_form.html'
    success_url = reverse_lazy('factura:factura_list')

    def form_valid(self, form):
        form.instance.fecha_emision = timezone.now().date()
        return super().form_valid(form)

class FacturaListView(LoginRequiredMixin, ListView):
    model = Factura
    template_name = 'factura/factura_list.html'
    context_object_name = 'facturas'

class FacturaDetailView(LoginRequiredMixin, DetailView):
    model = Factura
    template_name = 'factura/factura_detail.html'
    context_object_name = 'factura'

class FacturaUpdateView(LoginRequiredMixin, UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/factura_form.html'
    context_object_name = 'factura'
    success_url = reverse_lazy('factura:factura_list')

class FacturaDeleteView(LoginRequiredMixin, DeleteView):
    model = Factura
    template_name = 'factura/factura_delete.html'
    success_url = reverse_lazy('factura:factura_list')

class ItemFacturaCreateView(LoginRequiredMixin, CreateView):
    model = ItemFactura
    template_name = 'factura/itemfactura_form.html'
    fields = ['tipo', 'descripcion', 'monto']
    context_object_name = 'itemfactura'

    def form_valid(self, form):
        factura = get_object_or_404(Factura, pk=self.kwargs['factura_id'])
        form.instance.factura = factura
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('factura:factura_detail', kwargs={'pk': self.kwargs['factura_id']})
    
class ItemFacturaUpdateView(LoginRequiredMixin, UpdateView):
    model = ItemFactura
    form_class = ItemFacturaForm
    template_name = 'factura/itemfactura_form.html'
    context_object_name = 'itemfactura'

    def get_success_url(self):
        return self.object.factura.get_absolute_url()

class ItemFacturaDeleteView(LoginRequiredMixin, DeleteView):
    model = ItemFactura
    template_name = 'factura/itemfactura_delete.html'

    def get_success_url(self):
        return self.object.factura.get_absolute_url()
    