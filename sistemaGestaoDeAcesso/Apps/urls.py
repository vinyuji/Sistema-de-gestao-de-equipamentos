from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('equipamentos/', views.listar_equipamentos, name='listaEquipamentos'),
    path('pesquisar/', views.pesquisar, name= 'pesquisar'),
    path('perfil/', views.perfil, name= 'perfil'),
    path('acessibilidade/', views.acessibilidade, name= 'acessibilidade'),
    path('configuracao/', views.configuracao, name= 'configuracao'),
    path('historico/', views.historico, name= 'historico'),
]
