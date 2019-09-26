from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..api.models import Token


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        login = request.data.get('login', None)
        senha = request.data.get('senha', None)
        # app = request.POST.get('app', None)
        # os_player_id = request.POST.get('os_player_id', None)

        if login and senha:
            user = authenticate(request, matricula=login, password=senha)
            if user is not None:
                respond = {}

                # mobile nova
                # if os_player_id is not None:
                #     cria_lista_push(user.id, os_player_id)

                # try:
                #     nome_empresa = Parametro.objects.get(nome='NOME_EMPRESA_APP').valor
                # except:
                #     try:
                #         nome_empresa = Parametro.objects.get(nome='NOME_EMPRESA').valor
                #     except:
                #         nome_empresa = ''

                token = Token.objects.create(usuario_id=user.id)

                # verifica licença app rastreamento
                # try:
                #     equipamento = Equipamento.objects.get(uniqueid=user.licenca)
                #     respond['licenca'] = equipamento.id
                # except Equipamento.DoesNotExist:
                #     pass

                respond['id'] = user.id
                respond['token'] = token.token
                # respond['nome_empresa'] = nome_empresa

                return Response(respond)
            else:
                return Response({'msg': 'Usuário e/ou senha incorretos! :('})
        else:
            return Response({'msg': 'Informe Usuário ou Senha'})