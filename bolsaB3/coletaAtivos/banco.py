from .models import Ativos

def PrecosAcoes():
    return Ativos.objects.all()