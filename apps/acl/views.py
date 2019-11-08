from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
# Create your views here.
from ..usuario.forms import LoginForm, RegisterForm, ChangePasswordForm


def login_(request):
    if request.method == 'GET':
        if 'login' in request.session:
            return redirect('/')

    elif request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            matricula = form.cleaned_data['matricula']
            password = form.cleaned_data['password']

            user = authenticate(request, matricula=matricula, password=password)

            if user is not None:
                login(request, user)
                request.session['matricula'] = matricula
                return redirect('/')
        else:
            messages.error(request, _('Usuário ou senha inválidos! Tente novamente.'))

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, template_name='login/login.html', context=context)


def logout(request):
    request.session.flush()
    return redirect('acl:login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            matricula = form.cleaned_data.get('matricula', None)
            password = form.cleaned_data.get('password1', None)
            user = authenticate(request, matricula=matricula, password=password)
            if user is not None:
                login(request, user)
                request.session['matricula'] = matricula
                return redirect('/')
        else:
            messages.error(request, {'title': 'Erro!', 'submessage': 'Erro: {}'.format(form.error_messages.values())})

    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name='register/register.html', context=context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST)
        if form.is_valid():
            atual = form.cleaned_data.get('current_password')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                user = authenticate(request, matricula=request.user.matricula, password=atual)
                if user:
                    user.set_password(password2)
                    user.save()
                    login(request, user)
                    request.session['matricula'] = request.user.matricula
                    messages.success(request, {'title': 'Sucesso!', 'submessage': 'Senha alterada com Sucesso'})
                else:
                    messages.warning(request, {'title': 'Erro', 'submessage': 'Senha atual incorreta, tente novamente!'})
            else:
                messages.warning(request, {'title': 'Erro', 'submessage': 'As senhas não correspondem!'})
    form = ChangePasswordForm()
    context = {
        'form': form
    }
    return render(request, 'change_password/change_password.html', context)
