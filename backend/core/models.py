from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, help_text="Nome da categoria do produto")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Produto(models.Model):
    nome = models.CharField(max_length=200, help_text="Nome do produto")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    data_validade = models.DateField(help_text="Data de vencimento do produto")
    quantidade_disponivel = models.PositiveIntegerField(help_text="Quantidade em estoque")

    def __str__(self):
        return f"{self.nome} (Validade: {self.data_validade.strftime('%d/%m/%Y')})"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['data_validade']