from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Caso queira estender o usuário padrão:
class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('simples', 'Usuário Simples'),
        ('admin', 'Administrador'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='simples')

    def __str__(self):
        return self.username

class GrupoEquipamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    grupo = models.ForeignKey(GrupoEquipamento, on_delete=models.CASCADE, related_name='equipamentos')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class RegistroUso(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipamento.nome} usado por {self.usuario.username}"
