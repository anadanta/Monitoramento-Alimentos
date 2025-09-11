# Arquivo: core/models.py

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    
    data_validade = models.DateField(verbose_name="Data de Validade")
    quantidade_disponivel = models.PositiveIntegerField(default=0, verbose_name="Quantidade Disponível")
    data_de_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.quantidade_disponivel} em estoque)"