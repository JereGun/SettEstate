from django.urls import path
from imagen.views import ImagenPropiedadCreateView, ImagenPropiedadDeleteView
from .views import (
    PropiedadListView, PropiedadDeleteView, PropiedadDetailView, crear_propiedad, editar_propiedad
)

urlpatterns = [
    # URLs para Propiedad
    path('', PropiedadListView.as_view(), name='propiedad_list'),
    # path('create/', PropiedadCreateView.as_view(), name='propiedad_create'),
    path("create/", crear_propiedad, name="propiedad_create"),
    path("editar/<int:pk>/", editar_propiedad, name="propiedad_editar"),
    # path('update/<int:pk>/', PropiedadUpdateView.as_view(), name='propiedad_update'),
    path('delete/<int:pk>/', PropiedadDeleteView.as_view(), name='propiedad_delete'),
    path('detail/<int:pk>/', PropiedadDetailView.as_view(), name='propiedad_detail'),

    # URLs para ImagenPropiedad
    path('propiedad/<int:propiedad_id>/imagen/create/', ImagenPropiedadCreateView.as_view(), name='imagenpropiedad_create'),
    path('imagen/delete/<int:pk>/', ImagenPropiedadDeleteView.as_view(), name='imagenpropiedad_delete'),
]