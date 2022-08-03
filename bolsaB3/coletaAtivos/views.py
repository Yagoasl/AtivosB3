from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import ColetaAtivos
#from django.http import HttpResponse

def index(request):
    Acoes = ColetaAtivos.objects.all()

    dados = {
        'Acoes' : Acoes
    }
    return render(request, 'index.html', dados)

'''
def index(request):
    data_acoes = []
    a = TodasAcoes()
    for x in a:
        b = ColetaUltimoPrecoAcao(x.symbol)
        data_acoes.append((x.titulo, x.simbolo, b.preco, b.ask, b.bid, b.open_price, b.date_info))
    context = {
        'data_acoes': data_acoes,
    }
    template = loader.get_template('coletaAtivos/index.html')
    return HttpResponse(template.render(context, request))
'''
