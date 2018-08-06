from perfis.views import index, exibir, convidar, aceitar
from django.urls import path, re_path


urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='exibir'),
    re_path(r'^perfis/(?P<perfil_id>\d+)/convidar$', convidar, name='convidar'),
    re_path(r'^perfis/(?P<convite_id>\d+)/aceitar$', aceitar, name='aceitar'),
]
