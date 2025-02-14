from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Factura, ItemFactura


class FacturaCreateView(CreateView):
    model = Factura
    template_name = "factura/factura_form.html"
    fields = ['estado', 'fecha_vencimiento']
    context_object_name = 'factura'
    success_url = reverse_lazy('factura_list')

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
    template_name = 'factura/factura_form.html'
    fields = ['estado', 'fecha_vencimiento']
    context_object_name = 'factura'
    success_url = reverse_lazy('factura_list')

class FacturaDeleteView(LoginRequiredMixin, DeleteView):
    model = Factura
    template_name = 'factura/factura_delete.html'
    success_url = reverse_lazy('factura_list')

class ItemFacturaCreateView(LoginRequiredMixin, CreateView):
    model = ItemFactura
    template_name = 'factura/itemfactura_form.html'
    fields = ['descripcion', 'monto']
    context_object_name = 'itemfactura'

    def form_valid(self, form):
        factura = get_object_or_404(Factura, pk=self.kwargs['factura_id'])
        form.instance.factura = factura
        return super().form_valid(form)
    
class ItemFacturaUpdateView(LoginRequiredMixin, UpdateView):
    model = ItemFactura
    template_name = 'factura/itemfactura_form.html'
    fields = ['descripcion', 'monto']
    context_object_name = 'itemfactura'

    def get_success_url(self):
        return self.object.factura.get_absolute_url()

class ItemFacturaDeleteView(LoginRequiredMixin, DeleteView):
    model = ItemFactura
    template_name = 'factura/itemfactura_delete.html'

    def get_success_url(self):
        return self.object.factura.get_absolute_url()
    