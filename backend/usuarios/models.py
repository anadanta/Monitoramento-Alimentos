from django.db import models

class Segmento(models.TextChoices):
    SUPERMERCADO = "supermercado", "Supermercado"
    CONVENIENCIA = "conveniencia", "Conveniência"
    PADARIA = "padaria", "Padaria"
    RESTAURANTE = "restaurante", "Restaurante"
    OUTRO = "outro", "Outro"

class Usuarios(models.Model):
    nome_estabelecimento = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    segmento = models.CharField(max_length=100, choices=Segmento.choices)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_estabelecimento
    