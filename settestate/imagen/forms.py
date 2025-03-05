from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import ImagenPropiedad

class ImagenPropiedadForm(forms.ModelForm):
    class Meta:
        model = ImagenPropiedad()
        fields = ['imagen', 'descripcion', 'portada']
        widgets = {
            'descripcion': forms.TextInput(attrs={'placeholder': 'Breve descripción de la imagen'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('imagen', css_class='col-md-6'),
                Column('descripcion', css_class='col-md-4'),
                Column('portada', css_class='col-md-2 d-flex align-items-center'),
            )
        )