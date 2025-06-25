# DENTRO DE gestao_equipamentos/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Importe os nomes CORRETOS do seu models.py
from .models import Usuario, Ambiente, CategoriaEquipamento, Equipamento, Reserva

# Para customizar o que aparece no admin do nosso usuário
class CustomUserAdmin(UserAdmin):
    # Adiciona o campo 'tipo_usuario' no painel de admin ao criar e editar
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('tipo_usuario',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('tipo_usuario',)}),
    )

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_patrimonio', 'categoria', 'status')
    list_filter = ('status', 'categoria')
    search_fields = ('nome', 'codigo_patrimonio')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'solicitante', 'data_hora_inicio', 'data_hora_fim', 'status')
    list_filter = ('status', 'data_hora_inicio')
    search_fields = ('equipamento__nome', 'solicitante__username')


# Registra os modelos para que apareçam no painel de administração
admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Ambiente)
admin.site.register(CategoriaEquipamento)

# As linhas @admin.register(Equipamento) e @admin.register(Reserva) já fazem o registro
# para esses dois modelos, então não precisamos de admin.site.register para eles.