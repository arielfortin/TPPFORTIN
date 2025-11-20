from django.urls import path, include      # <-- include importado aquí
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.home, name='home'),
    path('profesionales/', views.professional_list, name='professional_list'),
    path('profesionales/nuevo/', views.professional_create, name='professional_create'),
    path('clientes/nuevo/', views.client_create, name='client_create'),
    path('citas/nuevo/', views.appointment_create, name='appointment_create'),
    path('accounts/', include('accounts.urls')),   
    path('profesionales/<int:pk>/editar/', views.professional_edit, name='professional_edit'),
    path('profesionales/<int:pk>/eliminar/', views.professional_delete, name='professional_delete'),
]
