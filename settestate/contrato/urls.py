from django.urls import path
from .views import ContratoListView, ContratoCreateView, ContratoUpdateView, ContratoDeleteView

urlpatterns = [
    path('', ContratoListView.as_view(), name='contrato_list'),
    path('create/', ContratoCreateView.as_view(), name='contrato_create'),
    path('update/<str:pk>/', ContratoUpdateView.as_view(), name='contrato_update'),
    path('delete/<str:pk>/', ContratoDeleteView.as_view(), name='contrato_delete'),
]
