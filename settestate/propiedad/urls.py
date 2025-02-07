from django.urls import path
from imagen.views import ImagenPropiedadCreateView, ImagenPropiedadDeleteView
from .views import (
    PropiedadListView, PropiedadCreateView, PropiedadUpdateView, PropiedadDeleteView, PropiedadDetailView,
    AtributoCreateView, AtributoDeleteView,
    ValorAtributoCreateView, ValorAtributoDeleteView
)

urlpatterns = [
    # URLs para Propiedad
    path('', PropiedadListView.as_view(), name='propiedad_list'),
    path('create/', PropiedadCreateView.as_view(), name='propiedad_create'),
    path('update/<int:pk>/', PropiedadUpdateView.as_view(), name='propiedad_update'),
    path('delete/<int:pk>/', PropiedadDeleteView.as_view(), name='propiedad_delete'),
    path('detail/<int:pk>/', PropiedadDetailView.as_view(), name='propiedad_detail'),

    # URLs para ImagenPropiedad
    path('propiedades/<int:propiedad_id>/imagen/create/', ImagenPropiedadCreateView.as_view(), name='imagenpropiedad_create'),
    path('imagen/delete/<int:pk>/', ImagenPropiedadDeleteView.as_view(), name='imagenpropiedad_delete'),

    # URLs para Atributo
    path('atributos/create/', AtributoCreateView.as_view(), name='atributo_create'),
    path('atributos/delete/<int:pk>/', AtributoDeleteView.as_view(), name='atributo_delete'),

    # URLs para ValorAtributo
    path('propiedades/<int:propiedad_id>/valoratributo/create/', ValorAtributoCreateView.as_view(), name='valoratributo_create'),
    path('valoratributo/delete/<int:pk>/', ValorAtributoDeleteView.as_view(), name='valoratributo_delete'),
]