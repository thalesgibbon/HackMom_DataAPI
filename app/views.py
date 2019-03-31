from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from funcao import funcao


class InsertAudio(APIView):
    def post(self, request):
        dicio = {}

        try:
            ''' salvar json '''
            body_dict = json.loads(str(request.body, encoding='utf-8'))

            audio = body_dict['audio']

            resultado = funcao(audio)

            if resultado:
                dicio = {'status': 'limit exceeded'}
            else:
                dicio = {'status': 'ok'}

        except:
            dicio = {'status': 'empty'}

        return Response(data=dicio, status=status.HTTP_200_OK)


def home(request):
    return render(request, 'app/home.html')
