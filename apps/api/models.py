import binascii
import os

from django.db import models

# Create your models here.
from ..usuario.models import Usuario


class Token(models.Model):
    '''
    app: 1=mobile; 2=web
    '''
    usuario = models.ForeignKey(Usuario, related_name='user_token_api', on_delete=models.SET_NULL, null=True)
    token = models.CharField(max_length=40, primary_key=True)
    # jidsession = models.CharField(max_length=128, unique=True)
    criado = models.DateTimeField(auto_now_add=True)
    # aplicacao = models.SmallIntegerField()

    class Meta:
        db_table = 'api_token'

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super(Token, self).save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __unicode__(self):
        return self.token
