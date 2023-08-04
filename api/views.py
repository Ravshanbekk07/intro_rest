from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

@api_view(['GET'])
def hello_world(request):
    return Response({'message':'hello world'})