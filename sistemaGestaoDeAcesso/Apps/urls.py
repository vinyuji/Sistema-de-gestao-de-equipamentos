from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipamentos/', views.listar_equipamentos, name='lista_equipamentos'),
]
