# Dentro de sistemaGestaoDeAcesso/urls.py
from django.contrib import admin
from django.urls import path, include # Adicione 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.urls')), # Adicione esta linha
]