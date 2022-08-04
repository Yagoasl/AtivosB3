from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Precos, Acoes
from django.http import HttpResponse
from .banco import TodasAcoes, AcaoDoSimbolo, ColetaUltimoPrecoAcao
from django.template import loader


def index(request):
    Acoes = Precos.objects.all()

    dados = {
        'Acoes' : Acoes
    }
    return render(request, 'index.html', dados)


# Infelizmente tive alguns problemas nesse def, mas esta proximo de funcionar
'''
def index(request):
    data_acoes = []
    a = TodasAcoes()
    for x in a:
        b = ColetaUltimoPrecoAcao(x.symbol)
        data_acoes.append((x.titulo, x.symbol, b.preco, b.open, b.date))
    dados = {
        'data_acoes': data_acoes,
    }
    template = loader.get_template('coletaAtivos/index.html')
    return HttpResponse(template.render(dados, request))
'''


