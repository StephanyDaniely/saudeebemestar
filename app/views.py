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
        return render(request, 'fisica.html', {'atividadesFisicas': atividadesFisicas})
    def post(self, request):
        pass

class AtividadeAlimentarView(View):
    def get(self, request, *args, **kwargs):
        atividadesAlimentares = AtividadeAlimentar.objects.all()
        return render(request, 'alimentar.html', {'atividadesAlimentares': atividadesAlimentares})
    def post(self, request):
        pass

class SaudeView(View):
    def get(self, request, *args, **kwargs):
        saude = Saude.objects.all()
        return render(request, 'saude.html', {'saude': saude})
    def post(self, request):
        pass

# class DeleteAtividadeFisica(View):
#     def get(self, request, id, *args, **kwargs):
#         atividadesFisicas = AtividadeFisica.objects.get(id=id)
#         atividadesFisicas.delete()
#         messages.success(request, 'Registro de atividade fisíca excluído com sucesso!')
#         return redirect('atividadesFisicas')
    
# class DeleteAtividadeAlimentar(View):
#     def get(self, request, id, *args, **kwargs):
#         atividadesAlimentares = AtividadeAlimentar.objects.get(id=id)
#         atividadesAlimentares.delete()
#         messages.success(request, 'Registro de atividade alimentar excluído com sucesso!')
#         return redirect('atividadesAlimentares')
    
# class DeleteSaude(View):
#     def get(self, request, id, *args, **kwargs):
#         saude = Saude.objects.get(id=id)
#         saude.delete()
#         messages.success(request, 'Registro de saúde fisíca e mental excluído com sucesso!')
#         return redirect('saude')