from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from scripts.master_reload import MasterReload


class InsertAudio(APIView):
    def post(self, request):
        url_audio = request.GET['url_audio']
        id_custumer = request.GET['id_custumer']
        key = f"{id_custumer}_{datetime.now().strftime('%Y%m%d_%H%M%S%f')}"

        try:
            retorno = MasterReload(k=key, c=id_custumer, a=url_audio).insert_return

            if retorno:
                dicio = {'status': 'ok'}
            else:
                dicio = {'status': 'falha'}
        except:
            dicio = {'status': 'empty'}

        return Response(data=dicio, status=status.HTTP_200_OK)


def home(request):
    return render(request, 'app/home.html')