from django.db import models

class Segmento(models.TextChoices):
    SUPERMERCADO = "supermercado", "Supermercado"
    CONVENIENCIA = "conveniencia", "Conveniência"
    PADARIA = "padaria", "Padaria"
    RESTAURANTES = "restaurantes", "Restaurantes"
    OUTRO = "outro", "Outro"

class Usuarios(models.Model):
    nome_usuario = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    segmento = models.CharField(max_length=100, choices=Segmento.choices)

    def __str__(self):
        return self.nome
    