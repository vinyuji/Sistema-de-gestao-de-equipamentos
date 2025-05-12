from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('configuracoes/', views.configuracoes, name='Configuracoes'),
    path('perfil/', views.perfil, name='Perfil'),
    path('consultas/', views.consultas, name='Consultas'),
    path('cadastros/', views.cadastros, name='Cadastros'),
    path('manual/', views.manual, name='Manual'),
    path('search/', views.search, name='Search'),
]