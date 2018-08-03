from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')


def exibir(request, perfil_id):
    perfil = Perfil()
    if(perfil_id == '1'):
        perfil = Perfil('Flavio Almeida', 'flavio@flavio.com.br', '777777', 'Caelum')
    return render(request, 'perfil.html', {"perfil": perfil})
