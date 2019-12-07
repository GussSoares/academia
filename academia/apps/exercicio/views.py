from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Create your views here.
from ..exercicio.models import Exercicio
from ..exercicio.forms import ExercicioForm


def list(request):
    exercicios = Exercicio.objects.all()
    context = {
        'exercicios': exercicios
    }
    template_name = 'exercicio/list.html'
    return render(request, template_name, context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create(request):
    if request.method == 'POST':
        form = ExercicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, {'title': 'Sucesso!', 'submessage': 'Informações salvas com sucesso!'})
        else:
            messages.warning(request, {'title': 'Erro!', 'submessage': 'Informe os campos corretamente!'})

    form = ExercicioForm()
    context = {
        'form': form
    }
    template_name = 'exercicio/create.html'
    return render(request, template_name, context)