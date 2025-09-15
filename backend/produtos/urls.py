# Arquivo: produtos/urls.py

from django.urls import path
from .views import lista_produtos, formulario_produtos

urlpatterns = [
    # URL para a página de listagem de produtos (Ex: http://127.0.0.1:8000/produtos/)
    path('', lista_produtos, name='lista_produtos'),
    
    # URL para a página do formulário (Ex: http://127.0.0.1:8000/produtos/formulario/)
    path('formulario/', formulario_produtos, name="formulario_produtos")]