from django.contrib import admin
from .models import Categorias, Transacao # É a nossa entidade modelo de base de dados

@admin.register(Categorias)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao') # Campos a serem exibidos
    search_fields  = ('nome',) # Campo de busca

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valor',  'categoria', 'data',  'descricao', 'saldo_total')
    search_fields  = ('tipo', 'descricao')