from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuit', 'telefono', 'email')
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'logo', 'cuit', 'telefono', 'email', 'sitio_web')
        }),
        ('Dirección', {
            'fields': ('direccion', 'ciudad', 'provincia', 'codigo_postal', 'pais')
        }),
        ('Información de Pago', {
            'fields': ('metodos_pago', 'cuenta_bancaria', 'cbu', 'alias')
        }),
    )
