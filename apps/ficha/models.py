from django.db import models

# Create your models here.
from ..usuario.models import Usuario
from ..exercicio.models import Exercicio
from ..core.models import TimeStampedModel


class Ficha(TimeStampedModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    # exercicio = models.ForeignKey(Exercicio, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ficha'


class FichaExercicio(TimeStampedModel):
    ficha = models.ForeignKey(Ficha, on_delete=models.SET_NULL, null=True)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ficha_exercicio'