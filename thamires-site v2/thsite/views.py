# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from thsite.models import Contato

# Create your views here.
def principal(request):
    template = loader.get_template('index.html')
    assunto = request.GET.get('assunto', '')
    nome_completo = request.GET.get('nome-completo', '')
    menssagem = request.GET.get('menssagem', '')
    contato = Contato(assunto = assunto, nome_completo = nome_completo, menssagem = menssagem)
    contato.save()

    return HttpResponse(template.render())