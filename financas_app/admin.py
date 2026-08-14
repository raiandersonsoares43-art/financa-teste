from django.contrib import admin
from .models import Transacao

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'tipo', 'data', 'usuario')
    list_filter = ('tipo', 'data', 'categoria')
    search_fields = ('descricao', 'categoria')