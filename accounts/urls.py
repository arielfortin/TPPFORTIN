from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('usuarios/', views.usuarios_view, name='usuarios'),
    path('perfil/', views.perfil_view, name='perfil'),
    path("registro/",views.registro, name='registro'),
    path('about/', views.about, name='about'),
]