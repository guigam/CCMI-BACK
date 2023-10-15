from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from ActualiteAPP.models import Actualite
from ActualiteAPP.serializers import ActualiteSerializer


# Create your views here.
class ActualiteList(generics.ListCreateAPIView):
    queryset = Actualite.objects.all()
    serializer_class = ActualiteSerializer
@csrf_exempt
def actualiteApi(request,id=0):
    if(request.method=='GET'):
        actualites = Actualite.objects.all()
        actualiteSerializer = ActualiteSerializer(actualites,many=True)
        return JsonResponse(actualiteSerializer.data,safe=False)
    elif request.method=='POST':
        actualite_data = JSONParser().parse(request)
        actualiteserializer = ActualiteSerializer(data = actualite_data)
        if(actualiteserializer.isValid()):
            actualiteserializer.save()
            return JsonResponse('success',safe = False)
        return JsonResponse('fail',safe=False)
