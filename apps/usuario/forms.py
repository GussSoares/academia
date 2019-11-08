from django import forms
from django.contrib.auth.forms import UsernameField
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.text import capfirst
from ..usuario.models import Usuario

UserModel = get_user_model()


class LoginForm(forms.Form):
    # login = forms.CharField(required=True, label='User Name', widget=forms.TextInput(attrs={
    #     'class': 'input-material',
    #     'data-msg': 'Please enter your username',
    #     'type': 'text',
    # }))
    # password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={
    #     'class': 'input-material',
    #     'data-msg': 'Please enter your password',
    #     'type': 'password'
    # }))

    matricula = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Matricula',
            'data-msg': 'Please enter your matricula',
            'type': 'text'
        }),
    )
    password = forms.CharField(
        # label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'data-msg': 'Please enter your password',
            'type': 'password'
        }),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(matricula)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['matricula'].label is None:
            self.fields['matricula'].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        matricula = self.cleaned_data.get('matricula')
        password = self.cleaned_data.get('password')

        if matricula is not None and password:
            self.user_cache = authenticate(self.request, matricula=matricula, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'matricula': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class RegisterForm(forms.ModelForm):
    # class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Informe uma senha',
            'data-msg': 'Please enter your password',
            'type': 'password'
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua senha',
            'data-msg': 'Please enter your password',
            'type': 'password'
        }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = Usuario
        fields = ("matricula", "first_name", "last_name", "email", 'password1', 'password2')
        field_classes = {'matricula': UsernameField}
        widgets = {
            'matricula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe sua matrícula',
                'data-msg': 'Please enter your matricula',
                'type': 'text',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe seu Nome',
                'data-msg': 'Please enter your First Name',
                'type': 'text'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe seu Sobrenome',
                'data-msg': 'Please enter your Last Name',
                'type': 'text'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe seu email',
                'data-msg': 'Please enter your Email',
                'type': 'email'
            })
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.matricula = self.cleaned_data.get('matricula')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    # password1 = forms.CharField(
    #     label=_("Password"), required=False,
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'form-control',
    #         'data-msg': 'Please enter your Password',
    #         'type': 'password',
    #     }),
    #     help_text=password_validation.password_validators_help_text_html(),
    # )
    # password2 = forms.CharField(
    #     label=_("Password confirmation"), required=False,
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'form-control',
    #         'data-msg': 'Please enter your Password',
    #         'type': 'password',
    #     }),
    #     strip=False,
    #     help_text=_("Enter the same password as before, for verification."),
    # )
    # profile = forms.ImageField(required=False, widget=forms.FileInput(attrs={
    #     'style': 'display: none',
    #     'type': 'file',
    #     # 'class': 'form-control',
    #     'accept': 'image/*'
    # }))

    class Meta:
        model = Usuario
        fields = ("first_name", "last_name", "matricula", "email", "is_superuser")
        widgets = {
            'matricula': forms.TextInput(attrs={
                'class': 'form-control',
                'data-msg': 'Please enter your matricula',
                'type': 'text',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'data-msg': 'Please enter your First Name',
                'type': 'text'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'data-msg': 'Please enter your Last Name',
                'type': 'text'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-msg': 'Please enter your Email',
                'type': 'email'
            }),
            'is_superuser': forms.CheckboxInput(attrs={
                'class': 'custom-control-input',
                'type': 'checkbox'
            }),
            # 'is_staff': forms.CheckboxInput(attrs={
            #     'class': 'checkbox-template',
            #     'type': 'checkbox'
            # }),
            # 'profile': forms.FileInput(attrs={
            #     'style': 'display: none',
            #     'type': 'file',
            #     # 'class': 'form-control',
            #     'accept': 'image/*'
            # })
        }

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #         )
    #     self.instance.username = self.cleaned_data.get('username')
    #     password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
    #     return password2

    # def save(self, commit=True):
    #     user = super(UserForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user


class ChangePasswordForm(UserForm):
    current_password = forms.CharField(
        label=_("Current Password"), required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'data-msg': 'Please enter your Password',
            'type': 'password',
        }),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    password1 = forms.CharField(
        label=_("Password"), required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'data-msg': 'Please enter your Password',
            'type': 'password',
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"), required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'data-msg': 'Please enter your Password',
            'type': 'password',
        }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = Usuario
        fields = []
    #     fields = ['email']
    #     widgets = {
    #         'email': forms.EmailInput(attrs={
    #             'class': 'form-control',
    #             'data-msg': 'Please enter your Email',
    #             'type': 'email',
    #             'required': 'true'
    #         }),
            # 'password1': forms.PasswordInput(attrs={
            #     'class': 'input-material',
            #     'data-msg': 'Please enter your Password',
            #     'type': 'password',
            #     'required': 'true'
            # }),
            # 'password2': forms.PasswordInput(attrs={
            #     'class': 'input-material',
            #     'data-msg': 'Please enter your Password',
            #     'type': 'password',
            #     'required': 'true'
            # }),
        # }

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)


class UserFilterForm(forms.Form):
    matricula = forms.CharField(max_length=254, required=False,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Informe o número de matrícula',
                                'data-msg': 'Please enter a matricula',
                                'type': 'text'
                            }))
    email = forms.EmailField(max_length=254, required=False,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Informe o email',
                                 'data-msg': 'Please enter a email',
                                 'type': 'email'
                             }))
    first_name = forms.CharField(max_length=254, required=False,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Informe o primeiro nome',
                                     'data-msg': 'Please enter a First Name',
                                     'type': 'text'
                                 }))
    status = forms.ChoiceField(required=False, label='Status', choices=(('0', 'Ativo'), ('1', 'Inativo'), ('2', 'Todos')),
                               widget=forms.Select(attrs={
                                   'class': 'form-control select2',
                                   'placeholder': '',
                                   'data-msg': 'Please enter a Status',

                               }))

    class Meta:
        model = Usuario
        fields = ['matricula', 'first_name', 'email']
        # widgets = {
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #         'data-msg': 'Please enter your Email',
        #         'type': 'email',
        #         'required': 'false'
        #     }),
        #     # 'username': forms.TextInput(attrs={
        #     #     'class': 'form-control',
        #     #     'data-msg': 'Please enter your username',
        #     #     'required': 'false'
        #     # }),
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'data-msg': 'Please enter your First Name',
        #         'required': 'false'
        #     }),
        # }
