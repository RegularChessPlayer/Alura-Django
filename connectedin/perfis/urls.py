from perfis.views import index, exibir
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='exibir'),
]
