from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

from ..api.utils import token_required
from ..usuario.models import Usuario
from rest_framework.decorators import api_view


@api_view(['GET'])
@token_required
def get_usuario(request, pk):
    try:
        usuario = Usuario.objects.filter(pk=pk).values('id', 'username', 'matricula', 'email', 'first_name', 'last_name',
                                                    'last_login', 'criado', 'modificado', 'is_superuser', 'is_active')
    except Usuario.DoesNotExist:
        return JsonResponse({"status": "404", "msg": "Usuário não existe"}, status=404,
                            encoder=DjangoJSONEncoder, safe=False)
    except Exception as exc:
        return JsonResponse({"status": "500", "msg": exc.args[0]}, status=500,
                            encoder=DjangoJSONEncoder, safe=False)
    return JsonResponse({"data": list(usuario), "status": "200"}, status=200, encoder=DjangoJSONEncoder, safe=False)
