from django.urls import re_path
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
    re_path(r'^login/$', auth_views.auth_login, {'template_name': 'login.html'}, name='login'),
    re_path(r'^logout/$', auth_views.logout_then_login, {'login_url':'/login/'}, name='logout'),
 
]