from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, related_name="perfil")

    @property
    def email(self):
        return self.usuario.email
    

    def convidar(self, perfil_logado):
        Convite(solicitante=self, convidado=perfil_logado).save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='convites_feito')
    convidado = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()
