from django.db import models

# Create your models here.
from academia.apps.usuario.models import Usuario
from academia.apps.exercicio.models import Exercicio


class Ficha(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ficha'
