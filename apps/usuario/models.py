from django.db import models
from django.core.mail import send_mail
from django.utils import six, timezone
# from passlib.hash import pbkdf2_sha256
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from ..core.models import TimeStampedModel
# from django.core.cache import cache
import datetime
from django.conf import settings


class UsuarioManager(BaseUserManager):
    def _create_user(self, matricula, email, password, **extra_fields):
        if not matricula:
            raise ValueError('The given matricula must be set')
        email = self.normalize_email(email)
        email = email or None
        matricula = self.model.normalize_username(matricula)
        user = self.model(matricula=matricula, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, matricula, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(matricula, email, password, **extra_fields)

    def create_superuser(self, matricula, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(matricula, email, password, **extra_fields)


# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin, TimeStampedModel):

    matricula = models.CharField(_('matricula'), max_length=7, unique=True, blank=None, null=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True,)
    email = models.EmailField(_('email'), blank=True, null=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    # profile = models.ImageField(upload_to='documents/', default='documents/avatar-generic.jpeg')
    # def verify_password(self, raw_password):
    #     return pbkdf2_sha256.verify(raw_password, self.password)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['email']

    objects = UsuarioManager()

    class Meta(AbstractUser.Meta):
        # swappable = 'AUTH_USER_MODEL'
        db_table = 'usuario'

    @property
    def get_full_name(self):
        return self.first_name+' '+self.last_name
    # def last_seen(self):
    #     return cache.get('seen_%s' % self.username)
    #
    # def online(self):
    #     if self.last_seen():
    #         now = datetime.datetime.now()
    #         if now > self.last_seen() + datetime.timedelta(
    #                 seconds=settings.USER_ONLINE_TIMEOUT):
    #             return False
    #         else:
    #             return True
    #     else:
    #         return False


'''###################### SERIALIZERS ######################'''


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        localized_fields = '__all__'
        fields = ('id', 'matricula', 'first_name', 'last_name', 'email', 'is_active')
