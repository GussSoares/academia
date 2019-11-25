import json
from functools import reduce

from django.core.serializers.json import DjangoJSONEncoder
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from rest_framework.renderers import JSONRenderer

from ..api.utils import token_required
from ..usuario.models import Usuario, UsuarioSerializer
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


@api_view(['POST', 'GET'])
def list_usuario_ajax(request):
    col_name = {
        '0': ['#id'],
        '1': ['#first_name'],
        '2': ['#last_name']
    }

    order_django = {  # ver como fazer a ordenação desc
        'asc': '',
        'desc': '-'
    }
    # tipo = request.GET.get('tipo')
    draw = request.GET.get('draw', '1')
    start = int(request.GET.get('start', '0'))
    length = int(request.GET.get('length', '10'))
    order_column = col_name[request.GET.get('order[0][column]', '0')]
    order_dir = order_django[request.GET.get('order[0][dir]', 'asc')]
    # order_column[-1]=order_dir+order_column[-1]

    erro = None
    # descricao = request.GET.get('descricao', None) or None
    # cliente = request.GET.get('cliente', None) or None
    # periodo = request.GET.get('periodo', None) or None
    # data_ini = request.GET.get('data_ini', None) or None
    # data_fim = request.GET.get('data_fim', None) or None
    # status = request.GET.get('status', None) or None
    # banco = request.GET.get('banco', None) or None
    # forma_pagamento = request.GET.get('forma_pagamento', None) or None
    # categoria = request.GET.get('categoria', None) or None
    # centro_custos = request.GET.get('centro_custos', None) or None

    queries = []
    try:
        # if descricao:
        #     queries.append(Q(conta__descricao__icontains=descricao))
        # if cliente:
        #     queries.append(Q(conta__cliente=int(cliente)))
        # if periodo and data_ini and data_fim:
        #     data_ini = datetime.date(datetime.strptime(data_ini, '%d/%m/%Y'))
        #     data_fim = datetime.date(datetime.strptime(data_fim, '%d/%m/%Y'))
        #     if data_fim < data_ini:
        #         raise Exception("Erro:", "Data fim não pode ser menor que data início.")
        #     if periodo == '1':  # Data vencimento
        #         queries.append(Q(data_vencimento__gte=data_ini))
        #         queries.append(Q(data_vencimento__lte=data_fim))
        #     if periodo == '2':  # Data Pagamento
        #         queries.append(Q(data_pagamento__gte=data_ini))
        #         queries.append(Q(data_pagamento__lte=data_fim))
        # if status != None:
        #     if status == '0':
        #         queries.append(Q(status__isnull=False))
        #     elif status == '3':
        #         queries.append(Q(status='2'))
        #         queries.append(Q(data_vencimento__lt=hoje()))
        #     elif status == '2':
        #         queries.append(Q(status=status))
        #         queries.append(Q(data_vencimento__gte=hoje()))
        #     else:  # status = 1
        #         queries.append(Q(status=status))
        # if banco:
        #     queries.append(Q(conta__banco=int(banco)))
        # if forma_pagamento:
        #     queries.append(Q(frm_pagamento=forma_pagamento))
        # if categoria:
        #     queries.append(Q(conta__categoria=int(categoria)))
        # if centro_custos:
        #     queries.append(Q(conta__centro_custos=int(centro_custos)))
        if queries:
            queries = reduce((lambda x, y: x & y), queries)
            # contas = list(ContaDetalhe.objects.filter(conta__tipo=tipo).filter(queries).order_by(
            #     *[c.replace('#', order_dir) for c in order_column]))
            usuarios = []
        else:
            # usuarios = list(ContaDetalhe.objects.filter(conta__tipo=tipo).all().exclude(status='1').order_by(
            #     *[c.replace('#', order_dir) for c in order_column]))
            usuarios = list(Usuario.objects.all().values('id', 'matricula', 'first_name', 'last_name', 'email', 'is_active').order_by(*[c.replace('#', order_dir) for c in order_column]))
            pass
    except Exception as exc:
        usuarios = []
        erro = str(exc)

    recordsTotal = len(usuarios)
    if length == -1:
        end = recordsTotal
    else:
        end = min(start + length, recordsTotal)
    # recordsFiltered = end-start
    recordsFiltered = recordsTotal
    usuarios_filtrado = usuarios[start:end]
    usuarios_serializer = UsuarioSerializer(usuarios_filtrado, many=True)
    dados_json_string = JSONRenderer().render(usuarios_serializer.data).decode('utf-8')
    dados_json_dict = json.loads(dados_json_string)

    response_json_dict = {
        'draw': draw,
        'recordsTotal': recordsTotal,
        'recordsFiltered': recordsFiltered,
    }
    if erro:
        response_json_dict['customActionMessage'] = erro
        response_json_dict['customActionStatus'] = 'ERRO'
    response_json_dict['data'] = dados_json_dict
    response_json_string = json.dumps(response_json_dict)
    http_resp = HttpResponse(response_json_string, content_type='application/json')
    return http_resp


@api_view(['GET', 'POST'])
def edit_usuario_ajax(request):
    id = request.GET.get('id')
    first = request.GET.get('first_name')
    last = request.GET.get('last_name')
    email = request.GET.get('email')

    try:
        usuario = Usuario.objects.get(id=int(id))
        usuario.first_name = first
        usuario.last_name = last
        usuario.email = email
        usuario.save()
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": _(exc.args[0])}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse(data={"msg": "Exercicio alterado com Sucesso", "status": "200"},
                        status=200, encoder=DjangoJSONEncoder, safe=False)