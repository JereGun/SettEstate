from django.shortcuts import render, redirect, get_object_or_404
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