from django.contrib import admin
from .models import Usuarios

@admin.register(Usuarios)
class UsarioAdmin(admin.ModelAdmin):
    list_display = ('nome_estabelecimento', 'email', 'segmento')
    search_fields = ('nome_estabelecimento', 'email')
