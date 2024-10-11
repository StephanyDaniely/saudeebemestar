from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})
    def post(self, request):
        pass

class TipoAtividadeFisicaView(View):
    def get(self, request, *args, **kwargs):
        tipoAtividade = TipoAtividadeFisica.objects.all()
        return render(request, 'tipoAtividade.html', {'tipoAtividade': tipoAtividade})
    def post(self, request):
        pass

class RefeicaoView(View):
    def get(self, request, *args, **kwargs):
        refeicao = Refeicao.objects.all()
        return render(request, 'refeicao.html', {'refeicao': refeicao})
    def post(self, request):
        pass

class AlimentoView(View):
    def get(self, request, *args, **kwargs):
        alimento = Alimento.objects.all()
        return render(request, 'alimento.html', {'alimento': alimento})
    def post(self, request):
        pass

class MedicamentoView(View):
    def get(self, request, *args, **kwargs):
        medicamento = Medicamento.objects.all()
        return render(request, 'medicamento.html', {'medicamento': medicamento})
    def post(self, request):
        pass

class AtividadeRelaxamentoView(View):
    def get(self, request, *args, **kwargs):
        relaxamento = AtividadeRelaxamento.objects.all()
        return render(request, 'relaxamento.html', {'relaxamento': relaxamento})
    def post(self, request):
        pass
    
class AtividadeFisicaView(View):
    def get(self, request, *args, **kwargs):
        atividadesFisicas = AtividadeFisica.objects.all()
        return render(request, 'atividadefisica.html', {'atividadesFisicas': atividadesFisicas})
    def post(self, request):
        pass

class AtividadeAlimentarView(View):
    def get(self, request, *args, **kwargs):
        atividadesAlimentares = AtividadeAlimentar.objects.all()
        return render(request, 'atividadealimentar.html', {'atividadesAlimentares': atividadesAlimentares})
    def post(self, request):
        pass

class SaudeView(View):
    def get(self, request, *args, **kwargs):
        saude = Saude.objects.all()
        return render(request, 'saude.html', {'saude': saude})
    def post(self, request):
        pass

class DadosView(View):
    def get(self,  request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        dados = []
        
        for usuario in usuarios:
            saude = Saude.objects.filter(usuario=usuario)
            atividadefisica = AtividadeFisica.objects.filter(usuario=usuario)
            atividadealimentar = AtividadeAlimentar.objects.filter(usuario=usuario)
            
            dados.append({
                'usuario': usuario,
                'saude': saude,
                'atividadefisica': atividadefisica,
                'atividadealimentar': atividadealimentar,
            })
        
        return render(request, 'dados.html', {'dados': dados})
