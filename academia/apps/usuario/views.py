from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

from ..usuario.forms import UserForm
from ..ficha.models import Ficha
from ..usuario.models import Usuario
import datetime

@login_required
# @user_passes_test(lambda u: u.is_superuser)
def list_user(request):
    users = Usuario.objects.all()
    context = {
        'users': users
    }
    template_name = 'usuario/list.html'
    return render(request, template_name, context)


@login_required
# @user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    pass


@login_required
def update_user(request):
    pass


# @login_required
# @user_passes_test(lambda u: u.is_superuser)
def delete_user(request):
    pass


@login_required()
def user_profile(request):
    instance = get_object_or_404(Usuario, pk=request.user.id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, {'title': 'Sucesso!', 'submessage': 'Informações atualizadas com sucesso!'})
        else:
            messages.warning(request, {'title': 'Erro!', 'submessage': 'Informe os campos corretamente!'})
    form = UserForm(instance=request.user)
    context = {
        'qtd_meses': datetime.date.today().month - request.user.criado.month,
        'qtd_fichas': len(Ficha.objects.filter(usuario_id=request.user.id)),
        'form': form
    }

    template_name = 'profile/profile.html'
    return render(request, template_name, context)