from django.urls import path
from .views import PersonaListView, PersonaCreateView, PersonaUpdateView, PersonaDeleteView

urlpatterns = [
    path('', PersonaListView.as_view(), name='persona_list'),
    path('create/', PersonaCreateView.as_view(), name='persona_create'),
    path('update/<str:pk>/', PersonaUpdateView.as_view(), name='persona_update'),
    path('delete/<str:pk>/', PersonaDeleteView.as_view(), name='persona_delete'),
]
