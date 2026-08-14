from django.db import models
from django.contrib.auth.models import User

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    data = models.DateField()
    categoria = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"