# -*- coding: utf-8 -*-
from django.db import models


class TimeStampedModel(models.Model):
    criado = models.DateTimeField('criado em', auto_now_add=True, auto_now=False, null=True)
    modificado = models.DateTimeField('modificado em', auto_now_add=False, auto_now=True, null=True)

    class Meta:
        abstract = True