# -*- coding: utf-8 -*-
from rest_framework.response import Response
from .models import Token


def token_required(func):
    def inner(request, *args, **kwargs):
        if request.method == 'OPTIONS':
            return func(request, *args, **kwargs)
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)

        if auth_header is not None:
            tokens = auth_header.split(' ')
            if len(tokens) == 2 and tokens[0] == 'token':
                token = tokens[1]
                try:
                    request.token = Token.objects.get(token=token)
                    return func(request, *args, **kwargs)
                except Token.DoesNotExist:
                    return Response({'msg': 'Token não existe'}, status=401)
            else:
                return Response({'msg': 'Token inválido'}, status=401)
        else:
            return Response({'msg': 'Header Inválido'}, status=401)

    return inner
