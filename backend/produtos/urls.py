from django.urls import path
from .views import *

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('formulario/', formulario_produtos, name="formulario_produtos"),
    path('deletar/<int:produto_id>', deletar_produto, name="deletar_produto")
]
