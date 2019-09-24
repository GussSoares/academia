from django.db import models

# Create your models here.
class Exercicio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "exercicio"
