from django.urls import path
from . import views
from .views import (
    FacturaListView, 
    FacturaCreateView, 
    FacturaUpdateView, 
    FacturaDetailView, 
    FacturaDeleteView, 
    ItemFacturaCreateView, 
    ItemFacturaUpdateView, 
    ItemFacturaDeleteView
)
app_name = 'factura'

urlpatterns = [
    # Urls Facturas
    path('', FacturaListView.as_view(), name='factura_list'),
    path('create/', FacturaCreateView.as_view(), name='factura_create'),
    path('detail/<str:pk>', FacturaDetailView.as_view(), name='factura_detail'),
    path('update/<str:pk>/', FacturaUpdateView.as_view(), name='factura_update'),
    path('delete/<str:pk>/', FacturaDeleteView.as_view(), name='factura_delete'),
    path('emitir/<int:pk>', views.emitir_factura, name='emitir_factura'),
    path('cancelar/<int:pk>', views.cancelar_factura, name='cancelar_factura'),
    path('pagar/<int:pk>', views.marcar_como_pagada, name='marcar_como_pagada'),
    path("borrador/<int:pk>", views.marcar_como_borrador, name="marcar_como_borrador"),
    path("factura/<int:pk>/pdf", views.factura_pdf_view, name="factura_pdf"),
    # Urls Item-Factura
    path('<int:factura_id>/item/create/', ItemFacturaCreateView.as_view(), name='itemfactura_create'),
    path('item/<int:pk>/update/', ItemFacturaUpdateView.as_view(), name='itemfactura_update'),
    path('item/<int:pk>/delete/', ItemFacturaDeleteView.as_view(), name='itemfactura_delete'),
]
