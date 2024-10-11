from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('usuarios/', UsuarioView.as_view(), name='usuarios'),
    path('atividadesFisicas/dados/', DadosView.as_view(), name='dados'),
    path('atividadesFisicas/index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('atividadesFisicas/saude/', SaudeView.as_view(), name='saude'),
    path('atividadesFisicas/', AtividadeFisicaView.as_view(), name='atividadesFisicas'),
    path('atividadesFisicas/atividadesAlimentares/', AtividadeAlimentarView.as_view(), name='atividadesAlimentares'),
    path('atividadesAlimentares/', AtividadeAlimentarView.as_view(), name='atividadesAlimentares'),
    path('atividadesAlimentares/dados/', DadosView.as_view(), name='dados'),
    path('atividadesAlimentares/saude/', SaudeView.as_view(), name='saude'),
    path('atividadesAlimentares/index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('atividadesAlimentares/atividadesFisicas/', AtividadeFisicaView.as_view(), name='atividadesFisicas'),
    path('saude/', SaudeView.as_view(), name='saude'),
    path('saude/dados/', DadosView.as_view(), name='dados'),
    path('saude/index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('saude/atividadesAlimentares/', AtividadeAlimentarView.as_view(), name='atividadesAlimentares'),
    path('saude/atividadesFisicas/', AtividadeFisicaView.as_view(), name='atividadesFisicas'),
    path('dados/', DadosView.as_view(), name='dados'),
    path('dados/saude/', SaudeView.as_view(), name='saude'),
    path('dados/index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('dados/atividadesFisicas/', AtividadeFisicaView.as_view(), name='atividadesFisicas'),
    path('dados/atividadesAlimentares/', AtividadeAlimentarView.as_view(), name='atividadesAlimentares'),
    
    path('tipoAtividade/', TipoAtividadeFisicaView.as_view(), name='tipoAtividade'),
    path('relaxamento/', AtividadeRelaxamentoView.as_view(), name='relaxamento'),
    path('refeicao/', RefeicaoView.as_view(), name='refeicao'),
    path('alimento/', AlimentoView.as_view(), name='alimento'),
    path('medicamento/', MedicamentoView.as_view(), name='medicamento'),
]
