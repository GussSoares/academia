from django.core.serializers.json import DjangoJSONEncoder
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.utils.translation import ugettext_lazy as _
from ..api.utils import token_required
from ..exercicio.models import Exercicio


@api_view(['GET'])
@token_required
def list_exercicios(request):
    try:
        exercicios = Exercicio.objects.all().values('id', 'nome', 'descricao', 'criado', 'modificado')
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"data": list(exercicios), "status": "200"}, status=200, encoder=DjangoJSONEncoder,
                        safe=False)


@api_view(['GET'])
@token_required
def get_exercicio(request, pk):
    try:
        exercicio = Exercicio.objects.filter(pk=pk).values('id', 'criado', 'modificado', 'nome', 'descricao')
        if len(exercicio):
            return JsonResponse(data={"data": list(exercicio), "status": "200"}, status=200, encoder=DjangoJSONEncoder,
                                safe=False)
        else:
            return JsonResponse({"status": "404", "msg": "Exercicio não existe"}, status=404,
                                encoder=DjangoJSONEncoder, safe=False)
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)


@api_view(['POST'])
@token_required
def create_exercicio(request):
    nome = request.data.get('nome', None)
    descricao = request.data.get('descricao', None)

    try:
        exercicio = Exercicio.objects.get(nome__icontains=nome.lower())
    except Exercicio.DoesNotExist:
        exercicio = Exercicio(nome=nome, descricao=descricao)
        exercicio.save()
        return JsonResponse(data={"msg": "Exercicio criado com Sucesso", "status": "200"},
                            status=200, encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"msg": "Exercicio com nome '{}' já existe".format(exercicio.nome), "status": "409"},
                        status=409, encoder=DjangoJSONEncoder, safe=False)


@api_view(['POST'])
@token_required
def update_exercicio(request, pk):
    o = get_object_or_404(Exercicio, pk=pk)
    nome = request.data.get('nome', None)
    descricao = request.data.get('descricao', None)

    try:
        if nome:
            o.nome = nome
        if descricao:
            o.descricao = descricao
        o.save()
    except IntegrityError as exc:
        if 'unique constraint' in exc.args[0]:
            return JsonResponse(data={"msg": "Exercicio com nome '{}' já existe".format(o.nome), "status": "409"},
                                status=409, encoder=DjangoJSONEncoder, safe=False)
        # else:
        #     return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
        #                         encoder=DjangoJSONEncoder, safe=False)
        raise Exception
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"msg": "Exercicio alterado com Sucesso", "status": "200"},
                        status=200, encoder=DjangoJSONEncoder, safe=False)