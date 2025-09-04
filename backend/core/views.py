from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as categorias sejam visualizadas ou editadas.
    """
    queryset = Categoria.objects.all().order_by('nome')
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os produtos sejam visualizados ou editados.
    """
    queryset = Produto.objects.all().order_by('data_validade')
    serializer_class = ProdutoSerializer