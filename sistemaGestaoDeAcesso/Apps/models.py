from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


class Usuario(AbstractUser):
    class TipoUsuario(models.TextChoices):
        SUPERUSUARIO = 'SUPERUSUARIO', 'Superusuário'
        PADRAO = 'PADRAO', 'Padrão'

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.PADRAO,
        verbose_name='Tipo de Usuário'
    )


class CategoriaEquipamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categorias de Equipamentos"

    def __str__(self):
        return self.nome
    
class Equipamento(models.Model):
    class Status(models.TextChoices):
        DISPONIVEL = 'DISPONIVEL', 'Disponível'
        EM_USO = 'EM_USO', 'Em Uso'
        EM_MANUTENCAO = 'EM_MANUTENCAO', 'Em Manutenção'

    nome = models.CharField(max_length=150)
    codigo_patrimonio = models.CharField(max_length=50, unique=True, verbose_name="Código de Patrimônio")
    categoria = models.ForeignKey(CategoriaEquipamento, on_delete=models.PROTECT, related_name='equipamentos')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DISPONIVEL)
    
    def __str__(self):
        return f"{self.nome} ({self.codigo_patrimonio})"



class Ambiente(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    equipamentos = models.ManyToManyField('Equipamento', through='AmbienteEquipamento', related_name='ambientes')

    def __str__(self):
        return self.nome
    
class AmbienteEquipamento(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)  

    class Meta:
        unique_together = ('ambiente', 'equipamento')

    def __str__(self):
        return f"{self.equipamento.nome} em {self.ambiente.nome} (Qtd: {self.quantidade})"


class Reserva(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        APROVADA = 'APROVADA', 'Aprovada'
        RECUSADA = 'RECUSADA', 'Recusada'
        CONCLUIDA = 'CONCLUIDA', 'Concluída'
        CANCELADA = 'CANCELADA', 'Cancelada'

    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='reservas')
    solicitante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservas_feitas')
    ambiente_uso = models.ForeignKey(Ambiente, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ambiente de Uso")
    data_hora_inicio = models.DateTimeField(verbose_name="Início")
    data_hora_fim = models.DateTimeField(verbose_name="Fim")
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Solicitação")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDENTE)

    def __str__(self):
        return f"Reserva de {self.equipamento.nome} por {self.solicitante.username}"

    # Garante que não haja sobreposição de reservas para o mesmo equipamento.
    def clean(self):
        super().clean()
        if self.data_hora_inicio and self.data_hora_fim:
            # Garante que a data final seja depois da inicial
            if self.data_hora_fim <= self.data_hora_inicio:
                raise ValidationError("A data/hora de fim deve ser posterior à de início.")
            
            # Garante que a reserva não seja no passado
            if self.data_hora_inicio < timezone.now():
                 raise ValidationError("Não é possível fazer uma reserva para uma data/hora no passado.")

            # Verifica se já existe outra reserva conflitante
            reservas_conflitantes = Reserva.objects.filter(
                equipamento=self.equipamento,
                status__in=[self.Status.APROVADA, self.Status.PENDENTE] # Apenas checa contra reservas válidas
            ).exclude(pk=self.pk) # Exclui a própria reserva se estiver sendo editada

            # Lógica de sobreposição de horários
            conflitos = reservas_conflitantes.filter(
                data_hora_inicio__lt=self.data_hora_fim,
                data_hora_fim__gt=self.data_hora_inicio
            )

            if conflitos.exists():
                raise ValidationError(
                    f"Este equipamento já está reservado ou com solicitação pendente para o período de {conflitos.first().data_hora_inicio.strftime('%d/%m/%Y %H:%M')} a {conflitos.first().data_hora_fim.strftime('%d/%m/%Y %H:%M')}."
                )