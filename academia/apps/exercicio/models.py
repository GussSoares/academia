from django.db import models
from ..core.models import TimeStampedModel
from rest_framework import serializers

# Create your models here.


class Exercicio(TimeStampedModel):
    nome = models.CharField(max_length=30, null=False, blank=False, unique=True)
    descricao = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "exercicio"


'''###################### SERIALIZERS ######################'''


class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        localized_fields = '__all__'
        fields = ('id', 'nome', 'descricao')
