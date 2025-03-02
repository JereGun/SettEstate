from django.urls import path
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
    # Urls Item-Factura
    path('<int:factura_id>/item/create/', ItemFacturaCreateView.as_view(), name='itemfactura_create'),
    path('item/<int:pk>/update/', ItemFacturaUpdateView.as_view(), name='itemfactura_update'),
    path('item/<int:pk>/delete/', ItemFacturaDeleteView.as_view(), name='itemfactura_delete'),
]
