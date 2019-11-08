from django.db import models
from ..core.models import TimeStampedModel


# Create your models here.
class Exercicio(TimeStampedModel):
    nome = models.CharField(max_length=30, null=False, blank=False, unique=True)
    descricao = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "exercicio"
