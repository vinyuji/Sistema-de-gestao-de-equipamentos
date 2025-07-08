# Dentro de Apps/views.py
from django.shortcuts import render
from .models import Equipamento, CategoriaEquipamento, Reserva, Ambiente
from django.db.models import Count, Q

def listar_equipamentos(request):
    nome = request.GET.get("nome", "")
    codigo = request.GET.get("codigo", "")
    categoria_id = request.GET.get("categoria", "")
    status = request.GET.get("status", "")

    equipamentos = Equipamento.objects.all()

    # Filtros
    if nome:
        equipamentos = equipamentos.filter(nome__icontains=nome)
    if codigo:
        equipamentos = equipamentos.filter(codigo_patrimonio__icontains=codigo)
    if categoria_id:
        equipamentos = equipamentos.filter(categoria_id=categoria_id)
    if status:
        equipamentos = equipamentos.filter(status=status)

    categorias = CategoriaEquipamento.objects.annotate(
        total_disponivel=Count(
            "equipamentos",
            filter=Q(equipamentos__status=Equipamento.Status.DISPONIVEL)
        )
    )

    context = {
        "equipamentos": equipamentos,
        "categorias": categorias,
        "valores": {
            "nome": nome,
            "codigo": codigo,
            "categoria_id": categoria_id,
            "status": status
        },
        "status_choices": Equipamento.Status.choices,
    }

    return render(request, "listarEquipamentos.html", context)

def home(request):
    return render(request, 'pages/home.html')


def historico(request):
    reservas = Reserva.objects.select_related('equipamento', 'solicitante', 'ambiente_uso').order_by('-data_solicitacao')

    context = {
        'reservas': reservas
    }
    return render(request, 'pages/historico.html', context)


def listar_ambientes(request):
    nome = request.GET.get('nome', '')
    ambientes = Ambiente.objects.all()
    if nome:
        ambientes = ambientes.filter(nome__icontains=nome)
    ambientes = ambientes.prefetch_related('ambienteequipamento_set__equipamento__categoria')
    return render(request, 'pages/ambiente.html', {'ambientes': ambientes})

def perfil(request):
    return render(request, 'pages/home.html')

def configuracao(request):
    return render(request, 'pages/home.html')

def acessibilidade(request):
    return render(request, 'pages/home.html')
