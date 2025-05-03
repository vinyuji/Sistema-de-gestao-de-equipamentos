from django.contrib import admin
from .models import Usuario, GrupoEquipamento, Equipamento, RegistroUso
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario, UserAdmin)
admin.site.register(GrupoEquipamento)
admin.site.register(Equipamento)
admin.site.register(RegistroUso)
