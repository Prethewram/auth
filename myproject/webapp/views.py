from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import logindb
from .serializers import loginserializer
import requests


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser



# Create your views here.
class loginlist(APIView):

    def get(self, request):
        login1=logindb.objects.all()
        serializer=loginserializer(login1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = loginserializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = logindb.objects.get(pk=pk)
        except logindb.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = loginserializer(instance, data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'msg': 'Data Updated'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            instance = logindb.objects.get(pk=pk)
        except logindb.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)

def loginpage(request):
    return render(request,"login.html")

