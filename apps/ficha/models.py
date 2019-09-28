from django.db import models

# Create your models here.
from ..usuario.models import Usuario
from ..exercicio.models import Exercicio
from ..core.models import TimeStampedModel


class Ficha(TimeStampedModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='usuario')
    instrutor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='instrutor')
    obs = models.TextField(null=True, blank=True)
    # exercicio = models.ForeignKey(Exercicio, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ficha'


class Treino(TimeStampedModel):
    titulo = models.CharField('Treino', max_length=3, null=False, blank=True)

    class Meta:
        db_table = 'treino'


class FichaExercicio(TimeStampedModel):
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE, null=True)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.SET_NULL, null=True)
    treino = models.ForeignKey(Treino, on_delete=models.SET_NULL, null=True)
    series = models.CharField('Séries', max_length=1, null=True, default=None)
    repeticoes = models.CharField('Repetições', max_length=2, null=True, default=None)

    class Meta:
        db_table = 'ficha_exercicio'


class FichaAtual(TimeStampedModel):
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ficha_atual'
