from django.db import models
from usuarios.models import Usuarios

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, help_text="Nome da categoria do produto")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class StatusProduto(models.TextChoices):
    NORMAL = "normal", "Normal"
    ATENCAO = "atencao", "Atenção"
    URGENTE = "urgente", "Urgente"
    VENCIDO = "vencido", "Vencido"
    VENDIDO = "vendido", "Vendido"

class UnidadeMedida(models.TextChoices):
    KG = "quilograma", "Quilograma"
    UN = "unidade", "Unidade"
    L = "litro", "Litro"

class Produto(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, help_text="Nome do produto")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    data_validade = models.DateField(help_text="Data de vencimento do produto")
    unidade_medida = models.CharField(max_length=20, choices=UnidadeMedida.choices, default=UnidadeMedida.UN, null=True, blank=True)
    quantidade_disponivel = models.PositiveIntegerField(help_text="Quantidade em estoque")
    status = models.CharField(max_length=20, choices=StatusProduto.choices, null=True, blank=True)
    codigo = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} (Validade: {self.data_validade.strftime('%d/%m/%Y')})"
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['data_validade']