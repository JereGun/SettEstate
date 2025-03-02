from django import forms
from .models import ActualizacionAlquiler, Contrato


class ContratoForm(forms.ModelForm):
    """Form definition for Contrato."""

    class Meta:
        """Meta definition for Contratoform."""

        model = Contrato
        fields = ('inquilino','propiedad','fecha_inicio', 'fecha_fin', 'frecuencia_actualizacion')
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'})
        }

class ActualizacionAlquilerForm(forms.ModelForm):
    class Meta:
        model = ActualizacionAlquiler
        fields = ['fecha_actualizacion', 'porcentaje_aumento']
        widgets = {
            'fecha_actualizacion': forms.DateInput(attrs={'type': 'date'})
        }