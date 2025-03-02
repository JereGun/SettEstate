from django import forms
from .models import Factura, ItemFactura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['contrato', 'fecha_vencimiento', 'estado']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes personalizar los campos aquí si es necesario
        self.fields['contrato'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_vencimiento'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})

class ItemFacturaForm(forms.ModelForm):
    class Meta:
        model = ItemFactura
        fields = ['tipo', 'descripcion', 'monto']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
