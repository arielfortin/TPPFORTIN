from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agenda.urls')),  # 👈 ruta principal va a la app agenda
]
