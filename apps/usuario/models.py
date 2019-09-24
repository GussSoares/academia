from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.db import models
from django.core.mail import send_mail
from django.utils import six, timezone
# from passlib.hash import pbkdf2_sha256
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
import datetime
from django.conf import settings


# Create your models here.
class Usuario(AbstractUser):
    # username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    # username = models.CharField(
    #     _('username'),
    #     max_length=150,
    #     unique=True,
    #     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[username_validator],
    #     error_messages={
    #         'unique': _("A user with that username already exists."),
    #     },
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    matricula = models.CharField(_('matricula'), max_length=7, unique=True, blank=None, null=None)
    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True,)
    email = models.EmailField(_('email address'), blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
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
    class Meta(AbstractUser.Meta):
        # swappable = 'AUTH_USER_MODEL'
        db_table = 'usuario'

    def last_seen(self):
        return cache.get('seen_%s' % self.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

