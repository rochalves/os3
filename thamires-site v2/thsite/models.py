# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contato(models.Model):
	assunto = models.CharField(max_length=20)
	nome_completo = models.CharField(max_length=40)
	menssagem = models.CharField(max_length=500)