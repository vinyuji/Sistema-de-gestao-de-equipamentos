from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Ambiente, Equipamento, CategoriaEquipamento, AmbienteEquipamento, Reserva

# Usuário com campo personalizado no admin
@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('tipo_usuario',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações adicionais', {'fields': ('tipo_usuario',)}),
    )
    list_display = ('username', 'email', 'tipo_usuario', 'is_staff')
    list_filter = ('tipo_usuario', 'is_staff')


# Equipamento
@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_patrimonio', 'categoria', 'status')
    list_filter = ('status', 'categoria')
    search_fields = ('nome', 'codigo_patrimonio')


# Categoria de Equipamento
@admin.register(CategoriaEquipamento)
class CategoriaEquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


# Ambiente
@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'total_equipamentos')
    search_fields = ('nome',)

    def total_equipamentos(self, obj):
        return obj.equipamentos.count()
    total_equipamentos.short_description = 'Nº Equipamentos'


# AmbienteEquipamento (intermediário)
@admin.register(AmbienteEquipamento)
class AmbienteEquipamentoAdmin(admin.ModelAdmin):
    list_display = ('ambiente', 'equipamento', 'quantidade')
    list_filter = ('ambiente', 'equipamento')
    search_fields = ('ambiente__nome', 'equipamento__nome')


# Reserva
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'solicitante', 'ambiente_uso', 'data_hora_inicio', 'data_hora_fim', 'status')
    list_filter = ('status', 'data_hora_inicio', 'ambiente_uso')
    search_fields = ('equipamento__nome', 'solicitante__username')
    date_hierarchy = 'data_hora_inicio'
