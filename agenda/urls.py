from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.home, name='home'),
    path('profesionales/', views.professional_list, name='professional_list'),
    path('profesionales/nuevo/', views.professional_create, name='professional_create'),
    path('clientes/nuevo/', views.client_create, name='client_create'),
    path('citas/nuevo/', views.appointment_create, name='appointment_create'),
]
