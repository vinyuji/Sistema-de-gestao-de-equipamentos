# Dentro de Apps/views.py
from django.shortcuts import render
from .models import Equipamento

def listar_equipamentos(request):
    # Busca todos os equipamentos no banco de dados
    equipamentos = Equipamento.objects.all().order_by('nome')

    # O "contexto" é um dicionário que leva os dados para o template
    contexto = {
        'lista_de_equipamentos': equipamentos
    }

    # Renderiza o arquivo HTML, enviando o contexto para ele
    return render(request, 'pages/listarEquipamentos.html', contexto)

def home(request):
    return render(request, 'pages/home.html')

def pesquisar(request):
    return render(request, 'pages/home.html')

def historico(request):
    return render(request, 'pages/home.html')

def perfil(request):
    return render(request, 'pages/home.html')

def configuracao(request):
    return render(request, 'pages/home.html')

def acessibilidade(request):
    return render(request, 'pages/home.html')
