from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from Apps import views
from .views import CustomLoginView



urlpatterns = [
    path('home/', views.home, name='home'),
    path('equipamentos/', views.listar_equipamentos, name='equipamentos'),
    path('ambiente/', views.listar_ambientes, name='ambiente'),
    path('perfil/', views.perfil, name= 'perfil'),
    path('acessibilidade/', views.acessibilidade, name= 'acessibilidade'),
    path('configuracao/', views.configuracao, name= 'configuracao'),
    path('historico/', views.historico, name= 'historico'),
    path('', CustomLoginView.as_view(), name='login'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('reservar/', views.reservar_equipamento, name='reservar_equipamento'),
    path('finalizar_reserva/', views.finalizar_reserva, name='finalizar_reserva'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
