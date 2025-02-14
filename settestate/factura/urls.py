from django.urls import path
from .views import FacturaListView, FacturaCreateView, FacturaUpdateView, FacturaDeleteView, ItemFacturaCreateView, ItemFacturaUpdateView, ItemFacturaDeleteView

urlpatterns = [
    path('', FacturaListView.as_view(), name='factura_list'),
    path('create/', FacturaCreateView.as_view(), name='factura_create'),
    path('update/<str:pk>/', FacturaUpdateView.as_view(), name='factura_update'),
    path('delete/<str:pk>/', FacturaDeleteView.as_view(), name='factura_delete'),
    path('item/create/', ItemFacturaCreateView.as_view(), name='itemfactura_create'),
    path('item/update/<str:pk>/', ItemFacturaUpdateView.as_view(), name='itemfactura_update'),
    path('item/delete/<str:pk>/', ItemFacturaDeleteView.as_view(), name='itemfactura_delete'),
]
