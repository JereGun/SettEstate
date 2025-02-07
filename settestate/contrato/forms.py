from django import forms
from .models import ActualizacionAlquiler

class ActualizacionAlquilerForm(forms.ModelForm):
    class Meta:
        model = ActualizacionAlquiler
        fields = ['fecha_actualizacion', 'porcentaje_aumento']