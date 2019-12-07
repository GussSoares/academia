from django.core.serializers.json import DjangoJSONEncoder
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from ..api.utils import token_required
from ..ficha.models import Ficha, FichaAtual,  FichaExercicio, Treino
from rest_framework.decorators import api_view


@api_view(['GET'])
@token_required
def list_treino(request):
    try:
        treinos = Treino.objects.all().values('id', 'criado', 'modificado', 'titulo')
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"data": list(treinos), "status": "200"}, status=200, encoder=DjangoJSONEncoder,
                        safe=False)


@api_view(['GET'])
@token_required
def get_usuario(request, pk):
    try:
        treino = Treino.objects.filter(pk=pk).values('id', 'criado', 'modificado', 'titulo')
    except Treino.DoesNotExist:
        return JsonResponse({"status": "404", "msg": "Treino não existe"}, status=404,
                            encoder=DjangoJSONEncoder, safe=False)
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": exc.args[0]}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"data": list(treino), "status": "200"}, status=200, encoder=DjangoJSONEncoder, safe=False)


@api_view(['POST'])
@token_required
def create_treino(request):
    titulo = request.data.get('titulo', None)

    try:
        treino = Treino.objects.get(titulo=titulo)
    except Treino.DoesNotExist:
        treino = Treino(titulo=titulo)
        treino.save()
        return JsonResponse(data={"msg": "Treino criado com Sucesso", "status": "200"},
                            status=200, encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"msg": "Treino com titulo '{}' já existe".format(treino.titulo), "status": "409"},
                        status=409, encoder=DjangoJSONEncoder, safe=False)


@api_view(['POST'])
@token_required
def update_treino(request, pk):
    o = get_object_or_404(Treino, pk=pk)
    titulo = request.data.get('titulo', None)

    try:
        if titulo:
            o.titulo = titulo
        o.save()
    except IntegrityError as exc:
        if 'unique constraint' in exc.args[0]:
            return JsonResponse(data={"msg": "Treino com titulo '{}' já existe".format(o.titulo), "status": "409"},
                                status=409, encoder=DjangoJSONEncoder, safe=False)
        else:
            return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                                encoder=DjangoJSONEncoder, safe=False)
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"msg": "Treino alterado com Sucesso", "status": "200"},
                        status=200, encoder=DjangoJSONEncoder, safe=False)
