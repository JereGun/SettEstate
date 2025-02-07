from django import forms
from django.core.exceptions import ValidationError
from .models import ImagenPropiedad

class ImagenPropiedadForm(forms.ModelForm):
    class Meta:
        model = ImagenPropiedad
        fields = ['imagen', 'portada']