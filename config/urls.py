from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('usuarios/', UsuarioView.as_view(), name='usuarios'),
    path('atividadesFisicas/', AtividadeFisicaView.as_view(), name='atividadesFisicas'),
    path('atividadesAlimentares/', AtividadeAlimentarView.as_view(), name='atividadesAlimentares'),
    path('saude/', SaudeView.as_view(), name='saude'),
]
