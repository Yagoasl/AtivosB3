'''Biblioteca para a interagir com o banco de dados'''

from .models import Precos, Acoes

def TodasAcoes():
    return Precos.objects.all()

def AcaoDoSimbolo(acao):
    return Precos.objects.get(symbol = acao)

def ColetaUltimoPrecoAcao(acao):
    box = AcaoDoSimbolo(acao)
    return Precos.objects.filter(acao=box)