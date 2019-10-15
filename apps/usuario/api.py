from django.core.serializers.json import DjangoJSONEncoder
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from ..api.utils import token_required
from ..usuario.models import Usuario
from rest_framework.decorators import api_view


@api_view(['GET'])
@token_required
def list_usuarios(request):
    try:
        usuarios = Usuario.objects.all().values('id', 'matricula', 'email', 'first_name', 'last_name',
                                                'last_login', 'criado', 'modificado', 'is_superuser', 'is_active')
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"data": list(usuarios), "status": "200"}, status=200, encoder=DjangoJSONEncoder,
                        safe=False)


@api_view(['GET'])
@token_required
def get_usuario(request, pk):
    try:
        usuario = Usuario.objects.filter(pk=pk).values('id', 'matricula', 'email', 'first_name', 'last_name',
                                                       'last_login', 'criado', 'modificado', 'is_superuser', 'is_active')
    except Usuario.DoesNotExist:
        return JsonResponse({"status": "404", "msg": "Usuário não existe"}, status=404,
                            encoder=DjangoJSONEncoder, safe=False)
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": exc.args[0]}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"data": list(usuario), "status": "200"}, status=200, encoder=DjangoJSONEncoder, safe=False)


@api_view(['POST'])
@token_required
def create_usuario(request):
    matricula = request.data.get('matricula', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    email = request.data.get('email', None)

    try:
        usuario = Usuario.objects.get(matricula=matricula)
    except Usuario.DoesNotExist:
        usuario = Usuario(matricula=matricula, first_name=first_name, last_login=last_name, email=email)
        usuario.save()
        return JsonResponse(data={"msg": "Usuário criado com Sucesso", "status": "200"},
                            status=200, encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"msg": "Usuário com matricula '{}' já existe".format(usuario.matricula), "status": "409"},
                        status=409, encoder=DjangoJSONEncoder, safe=False)


@api_view(['POST'])
@token_required
def update_usuario(request, pk):
    o = get_object_or_404(Usuario, pk=pk)
    # matricula = request.data.get('matricula', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    email = request.data.get('email', None)

    try:
        # if matricula:
        #     o.matricula = matricula
        if first_name:
            o.first_name = first_name
        if last_name:
            o.last_name = last_name
        if email:
            o.email = email
        o.save()
    except IntegrityError as exc:
        if 'unique constraint' in exc.args[0]:
            return JsonResponse(data={"msg": "Usuário com matricula '{}' já existe".format(o.matricula), "status": "409"},
                                status=409, encoder=DjangoJSONEncoder, safe=False)
        else:
            return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                                encoder=DjangoJSONEncoder, safe=False)
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"msg": "Usuário alterado com Sucesso", "status": "200"},
                        status=200, encoder=DjangoJSONEncoder, safe=False)
