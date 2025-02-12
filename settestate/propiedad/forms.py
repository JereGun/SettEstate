from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Propiedad

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'fecha_creacion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_actualizacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))
