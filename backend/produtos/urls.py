# Arquivo: produtos/urls.py

from django.urls import path
from .views import lista_produtos, formulario_produtos

urlpatterns = [
    # URL para a página de listagem de produtos (Ex: http://127.0.0.1:8000/produtos/)
    path('', lista_produtos, name='lista_produtos'),
    path('formulario/', formulario_produtos, name="formulario_produtos"),
    path('deletar/<int:produto_id>', deletar_produto, name="deletar_produto")
]
