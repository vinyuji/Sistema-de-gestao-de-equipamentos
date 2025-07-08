from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('equipamentos/', views.listar_equipamentos, name='equipamentos'),
    path('ambiente/', views.listar_ambientes, name='ambiente'),
    path('perfil/', views.perfil, name= 'perfil'),
    path('acessibilidade/', views.acessibilidade, name= 'acessibilidade'),
    path('configuracao/', views.configuracao, name= 'configuracao'),
    path('historico/', views.historico, name= 'historico'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
