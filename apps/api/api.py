from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..api.models import Token


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        matricula = request.data.get('matricula', None)
        senha = request.data.get('senha', None)

        if login and senha:
            user = authenticate(request, matricula=matricula, password=senha)
            if user is not None:
                respond = {}

                token = Token.objects.create(usuario_id=user.id)

                respond['id'] = user.id
                respond['token'] = token.token

                return Response(respond)
            else:
                return Response({'msg': 'Usuário e/ou senha incorretos! :('})
        else:
            return Response({'msg': 'Informe Usuário ou Senha'})