from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,  Row, Column, Fieldset, HTML
from crispy_forms.bootstrap import TabHolder, Tab, PrependedText, AppendedText
from .models import Propiedad

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describa las características principales de la propiedad...'}),
            'fecha_creacion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_actualizacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        
        self.helper.layout = Layout(
            TabHolder(
                Tab('Información Básica',
                    Fieldset('Datos generales',
                        Row(
                            Column('denominacion', css_class='col-md-6'),
                            Column('tipo', css_class='col-md-6'),
                        ),
                        'descripcion',
                    ),
                ),
                Tab('Ubicación',
                    Fieldset('Dirección',
                        Row(
                            Column('calle', css_class='col-md-8'),
                            Column('numeracion', css_class='col-md-4'),
                        ),
                        Row(
                            Column('ciudad', css_class='col-md-6'),
                            Column('provincia', css_class='col-md-6'),
                        ),
                        Row(
                            Column('piso', css_class='col-md-4'),
                            Column('departamento', css_class='col-md-4'),
                            Column('codigo_postal', css_class='col-md-4'),
                        ),
                    ),
                    HTML('<div class="mt-3 mb-3"><div id="map" style="height: 300px; width: 100%;"></div></div>'),
                ),
                Tab('Datos de Contrato',
                        Row(
                            Column(PrependedText('precio', '$'), css_class='col-md-6'),
                            Column(AppendedText('superficie', 'm²'), css_class='col-md-6'),
                        ),
                        Row(
                            Column('estado', css_class='col-md-6'),
                            Column('propietario', css_class='col-md-6'),
                        ),
                ),
                Tab('Características',
                    Fieldset('Detalles',
                        Row(
                            Column('dormitorios', css_class='col-md-4'),
                            Column('ambientes', css_class='col-md-4'),
                            Column('baños', css_class='col-md-4'),
                            Column('cocheras', css_class='col-md-4'),
                            Column('antiguedad', css_class='col-md-4'),
                            Column('pisos', css_class='col-md-4'),
                            Column('metros_cubiertos', css_class='col-md-4'),
                            Column('metros_descubiertos', css_class='col-md-4'),
                            Column('metros_totales', css_class='col-md-4'),
                        ),
                    ),
                ),
                Tab('Fechas y Documentación',
                    Fieldset('Control de fechas',
                        Row(
                            Column('creacion', css_class='col-md-6'),
                            Column('ultima_actualizacion', css_class='col-md-6'),
                        ),
                    ),
                    Fieldset('Documentación',
                        Row(
                            Column('escritura', css_class='col-md-6'),
                            Column('impuestos_al_dia', css_class='col-md-6'),
                        ),
                    ),
                ),
            ),
        )