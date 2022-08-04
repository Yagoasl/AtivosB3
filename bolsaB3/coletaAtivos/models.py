from django.db import models
from datetime import datetime

class Acoes(models.Model):
    symbol = models.CharField(max_length=10)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(("Descrição Aqui"))

    def __str__(self):
        return self.symbol  

class Precos(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateTimeField('data publicada')
    low = models.FloatField()
    open = models.FloatField()
    volume = models.FloatField()
    high = models.FloatField()
    close = models.FloatField()
    adjclose = models.FloatField()

'''
class Ativos(models.Model):
    codigo = models.CharField(max_length=100)
    preco = models.FloatField()
    variacao_porcento = models.FloatField()
    variacao = models.FloatField()
    tendencia = models.CharField(max_length=100)
    volume = models.FloatField()
    volume_preco = models.FloatField()
    valor = models.FloatField()
    pl = models.FloatField()
    eps = models.FloatField()
    funcionarios = models.FloatField()
    setor = models.CharField(max_length=100)
'''