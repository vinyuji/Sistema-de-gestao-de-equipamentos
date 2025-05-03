from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento, RegistroUso
from .forms import EquipamentoForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'gerenciamento/lista_equipamentos.html', {'equipamentos': equipamentos})

@login_required
def alugar_equipamento_view(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if equipamento.disponivel:
        RegistroUso.objects.create(equipamento=equipamento, usuario=request.user)
        equipamento.disponivel = False
        equipamento.save()
    return redirect('gerenciamento:lista_equipamentos')

@login_required
def devolver_equipamento_view(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    registro = RegistroUso.objects.filter(equipamento=equipamento, usuario=request.user, data_fim__isnull=True).last()
    if registro:
        registro.data_fim = timezone.now()
        equipamento.disponivel = True
        equipamento.save()
        registro.save()
    return redirect('gerenciamento:lista_equipamentos')

@login_required
def novo_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.disponivel = True
            equipamento.save()
            return redirect('gerenciamento:lista_equipamentos')
    else:
        form = EquipamentoForm()
    return render(request, 'gerenciamento/novo_equipamento.html', {'form': form})
