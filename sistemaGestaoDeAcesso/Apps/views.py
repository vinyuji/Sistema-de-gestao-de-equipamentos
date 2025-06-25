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
    return render(request, 'Apps/listar_equipamentos.html', contexto)