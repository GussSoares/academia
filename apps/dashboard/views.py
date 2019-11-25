from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from ..usuario.models import Usuario

# Create your views here.


@login_required
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    count_user = Usuario.objects.all().count()
    context = {
        'users': count_user
    }
    return render(request, 'dashboard/index.html', context)