# Dentro de Apps/views.py
from django.shortcuts import render, redirect
from .models import Equipamento, CategoriaEquipamento, Reserva, Ambiente
from django.db.models import Count, Q
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.utils import timezone
from django.utils.timezone import now

class CustomLoginView(LoginView):
    template_name = 'pages/login.html'


@login_required
@require_POST
def reservar_equipamento(request):
    equipamento_id = request.POST.get("equipamento_id")
    ambiente_id = request.POST.get("ambiente_id", None)  # Opcional

    equipamento = get_object_or_404(Equipamento, id=equipamento_id)

    if equipamento.status != Equipamento.Status.DISPONIVEL:
        messages.error(request, "Equipamento não está disponível.")
        return redirect("equipamentos")

    ambiente = Ambiente.objects.filter(id=ambiente_id).first() if ambiente_id else None

    Reserva.objects.create(
        equipamento=equipamento,
        solicitante=request.user,
        ambiente_uso=ambiente,
        data_hora_inicio=timezone.now(),
        data_hora_fim=timezone.now() + timezone.timedelta(hours=2),  # tempo fixo, pode ser ajustado
        status=Reserva.Status.APROVADA
    )

    equipamento.status = Equipamento.Status.EM_USO
    equipamento.save()

    messages.success(request, "Reserva realizada com sucesso!")
    return redirect("historico")


@login_required
@require_POST
def finalizar_reserva(request):
    reserva_id = request.POST.get("reserva_id")
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

    if not reserva.data_hora_fim:
        reserva.data_hora_fim = timezone.now()
        reserva.status = 'FINALIZADA'
        reserva.save()

        # Liberar o equipamento para novos usuários
        equipamento = reserva.equipamento
        equipamento.status = 'DISPONIVEL'
        equipamento.save()

    return redirect('perfil') 


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


# @login_required
# def perfil(request):
#     reservas = Reserva.objects.filter(solicitante=request.user).select_related('equipamento', 'ambiente_uso').order_by('-data_solicitacao')
#     return render(request, 'pages/perfil.html', {'reservas': reservas})

@login_required
def perfil(request):
    usuario = request.user

    reservas_ativas = Reserva.objects.filter(solicitante=usuario, status='PENDENTE')
    reservas_finalizadas = Reserva.objects.filter(solicitante=usuario, status='FINALIZADA')

    return render(request, 'pages/perfil.html', {
        'reservas': reservas_ativas,      # Ativos
        'historico': reservas_finalizadas  # Já finalizados
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('perfil')  # Redireciona para o perfil após login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})


def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso. Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os campos.')
    else:
        form = UserCreationForm()
    return render(request, 'pages/cadastro.html', {'form': form})

def configuracao(request):
    return render(request, 'pages/home.html')

def acessibilidade(request):
    return render(request, 'pages/home.html')
