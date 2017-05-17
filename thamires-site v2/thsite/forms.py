from django import forms

class ContatoForm(forms.Form):
	assunto = forms.CharField()
	nome_completo = forms.CharField()
	menssagem = forms.CharField()
