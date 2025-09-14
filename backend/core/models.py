from django.db import models
from usuarios.models import Usuarios
from datetime import datetime
from django.utils import timezone

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
    KG = "quilograma", "Quilograma (Kg)"
    UN = "unidade", "Unidade (1)"
    L = "litro", "Litro (L)"

class CategoriaProduto(models.TextChoices):
    ALIMENTOS = "alimentos", "Alimentos"
    BEBIDAS = "bebidas", "Bebidas"
    LIMPEZA = "limpeza", "Limpeza"
    HIGIENE = "higiene", "Higiene"
    OUTROS = "outros", "Outros"

class Produto(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200, help_text="Nome do produto")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    data_validade = models.DateField(help_text="Data de vencimento do produto")
    quantidade_disponivel = models.PositiveIntegerField(help_text="Quantidade em estoque")
    unidade_medida = models.CharField(max_length=20, choices=UnidadeMedida.choices, default=UnidadeMedida.UN, null=True, blank=True)
    status = models.CharField(max_length=20, choices=StatusProduto.choices, null=True, blank=True)
    codigo = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} (Validade: {self.data_validade.strftime('%d/%m/%Y')})"
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['data_validade']

    def verificar_status(self):
        if self.quantidade_disponivel == 0:
            self.status = StatusProduto.VENDIDO
            return
        
        hoje = datetime.now().date()
        data_validade = self.data_validade

        # garante que seja sempre date
        if isinstance(data_validade, datetime):
            data_validade = data_validade.date()
        
        dias_restantes = (data_validade - hoje).days

        if dias_restantes >= 90:
            self.status = StatusProduto.NORMAL
        elif 30 < dias_restantes < 90:
            self.status = StatusProduto.ATENCAO
        elif 1 <= dias_restantes <= 30:
            self.status = StatusProduto.URGENTE
        elif dias_restantes <= 0:
            self.status = StatusProduto.VENCIDO
        else:
            self.status = StatusProduto.NORMAL

    def save(self, *args, **kwargs):
        if self.data_validade:
            self.verificar_status()
        super().save(*args, **kwargs)

    # Esse método será usado em conjunto com o selenium para rodar diariamente e atualizar os status da base de dados
    @property
    def dias_para_vencer(self):
        """Propriedade para obter dias restantes"""
        if self.data_validade:
            return (self.data_validade - timezone.now().date()).days
        return None