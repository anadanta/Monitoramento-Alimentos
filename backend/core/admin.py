from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.

# Registra o modelo Categoria no painel de admin
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

# Registra o modelo Produto no painel de admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'data_validade', 'quantidade_disponivel')
    search_fields = ('nome', 'categoria__nome')
    list_filter = ('categoria', 'data_validade')
