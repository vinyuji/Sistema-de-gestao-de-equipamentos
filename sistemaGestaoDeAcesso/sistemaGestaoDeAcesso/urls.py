from django.urls import path
from Apps import views

app_name = 'gerenciamento'  # Define o namespace para as URLs, se for necessário

urlpatterns = [
    path('', views.home, name='home'),
    # path('equipamentos/', views.lista_equipamentos, name='lista_equipamentos'),
    # path('equipamento/<int:pk>/alugar/', views.alugar_equipamento_view, name='alugar_equipamento'),
    # path('equipamento/<int:pk>/devolver/', views.devolver_equipamento_view, name='devolver_equipamento'),
    # path('equipamento/novo/', views.novo_equipamento, name='novo_equipamento'),
]