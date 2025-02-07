from django.contrib import admin
from .models import Propiedad, Atributo, ValorAtributo

admin.site.register(Propiedad)
admin.site.register(Atributo)
admin.site.register(ValorAtributo)