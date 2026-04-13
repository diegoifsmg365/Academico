"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cidades/', CidadeView.as_view(), name='cidades'),
    path('ocupacoes/', OcupacaoView.as_view(), name='ocupacoes'),
    path('pessoas/', PessoaView.as_view(), name='pessoas'),
    path('instituicoes/', InstituicaoEnsinoView.as_view(), name='instituicoes'),
    path('areas/', AreaSaberView.as_view(), name='areas'),
    path('cursos/', CursoView.as_view(), name='cursos'),
    path('turmas/', TurmaView.as_view(), name='turmas'),
    path('disciplinas/', DisciplinaView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculaView.as_view(), name='matriculas'),
    path('tipos-avaliacao/', AvaliacaoTipoView.as_view(), name='tipos_avaliacao'),
    path('avaliacoes/', AvaliacaoView.as_view(), name='avaliacoes'),
    path('frequencias/', FrequenciaView.as_view(), name='frequencias'),
    path('turnos/', TurnoView.as_view(), name='turnos'),
    path('ocorrencias/', OcorrenciaView.as_view(), name='ocorrencias'),
    path('cursos-disciplinas/', CursoDisciplinaView.as_view(), name='cursos_disciplinas'),
]