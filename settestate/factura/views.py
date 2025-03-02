from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Factura, ItemFactura
from .forms import FacturaForm, ItemFacturaForm, ItemFacturaFormSet
from .utils import render_to_pdf

# Vistas de Factura
class FacturaCreateView(LoginRequiredMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/factura_form.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = ItemFacturaFormSet()
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = ItemFacturaFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)
    
    def form_valid(self, form, formset):
        form.instance.fecha_emision = timezone.now().date()
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.get_success_url())
    
    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )
    
    def get_success_url(self):
        return reverse_lazy('factura:factura_list')

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ItemFacturaFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context['formset'] = ItemFacturaFormSet(instance=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = ItemFacturaFormSet(request.POST, instance=self.object)
        
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)
    
    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        messages.success(self.request, "Factura actualizada correctamente")
        return redirect(self.get_success_url())
    
    def form_invalid(self, form, formset):
        messages.error(self.request, "Hubo errores al actualizar la factura")
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )
    
    def get_success_url(self):
        return reverse_lazy('factura:factura_list')

class FacturaDeleteView(LoginRequiredMixin, DeleteView):
    model = Factura
    template_name = 'factura/factura_delete.html'
    success_url = reverse_lazy('factura:factura_list')

def emitir_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if factura.es_editable():
        factura.emitir()
        messages.success(request, "Factura emitida correctamente.")
    else:
        messages.error(request, "La factura no puede ser emitida.")
    return redirect('factura:factura_detail', pk=factura.pk)

def cancelar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    factura.anular()
    messages.success(request, "Factura cancelada.")
    return redirect('factura:factura_detail', pk=factura.pk)

def marcar_como_pagada(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if factura.estado == 'EMITIDA':
        factura.marcar_pagada()
        messages.success(request, "Factura marcada como pagada.")
    else:
        messages.error(request, "Solo facturas emitidas pueden ser marcadas como pagadas.")
    return redirect('factura:factura_detail', pk=factura.pk)

def marcar_como_borrador(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if factura.estado in ['EMITIDA', 'PAGADA', 'ANULADA']:
        factura.marcar_borrador()
        messages.success(request, "Factura establecida como borrador")
    return redirect('factura:factura_detail', pk=pk)

def factura_pdf_view(request, pk):
    """Vista para generar un PDF de la factura"""
    factura = get_object_or_404(Factura, pk=pk)
    
    # Generar el PDF
    pdf = render_to_pdf('factura/factura_pdf.html', {'factura': factura})
    
    # Configurar la respuesta para descargar el archivo
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"Factura_{factura.numero}.pdf"
        content = f"attachment; filename={filename}"
        response['Content-Disposition'] = content
        return response
    
    # En caso de error
    return HttpResponse("Error al generar el PDF", status=400)

# Vistas de ItemFactura
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
    