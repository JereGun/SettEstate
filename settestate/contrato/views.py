from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contrato
from .forms import ActualizacionAlquilerForm

def registrar_actualizacion(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    if request.method == 'POST':
        form = ActualizacionAlquilerForm(request.POST)
        if form.is_valid():
            actualizacion = form.save(commit=False)
            actualizacion.contrato = contrato
            actualizacion.save()
            return redirect('detalle_contrato', contrato_id=contrato.id)
    else:
        form = ActualizacionAlquilerForm()
    return render(request, 'registrar_actualizacion.html', {'form': form, 'contrato': contrato})


class ContratoListView(ListView):
    model = Contrato
    template_name = "contrato_list.html"
    context_object_name = "contratos"


class ContratoUpdateView(UpdateView):
    model = Contrato
    template_name = "contrato_update.html"

class ContratoDeleteView(DeleteView):
    model = Contrato
    template_name = "contrato_delete.html"
    success_url = "/contrato/"

class ContratoCreateView(CreateView):
    model = Contrato
    template_name = "contrato_create.html"
    fields = '__all__'
    success_url = "/contrato/"
