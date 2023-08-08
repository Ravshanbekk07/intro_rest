from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Task
from django.forms.models import model_to_dict




@api_view(['GET','POST'])
def getask(request:Request,title=None)-> Response:
    if request.method == 'GET':
        if title is None:
            tasks = Task.objects.all()
            task_dic = [model_to_dict(task) for task in tasks]
            return Response(task_dic,status=status.HTTP_200_OK)
        else:
            try:
                

                
                task = Task.objects.get(title=title)
                
                task_dict = model_to_dict(task)
                return Response(task_dict,status=status.HTTP_200_OK)
            except Task.DoesNotExist:
                return Response({'error':'task not found'},status=status.HTTP_404_NOT_FOUND) 

@api_view(['POST'])   
def postask(request):
    if request.method == 'POST':
        data =request.data
        try:
            task = Task.objects.create(
                title = data.get('title'),
                description = data.get('description'))
            task.save()
            return Response(model_to_dict(task),status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({'error':'invalid data'},status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT'])      
def putask(request,pk):
    if request.method == 'PUT':
        if pk is None:
                return Response({'error': 'Invalid request'}, status=400)
        else:
            try:
                data =request.data

                task = Task.objects.get(pk=pk)
                task.title = data.get('title')
                
                task.description = data.get('description')
                task.save()
                return Response(model_to_dict(task),status=status.HTTP_200_OK)
            except KeyError:
                return Response({'error':'invalid data'})
@api_view(['DELETE'])        
def deletetask(request,pk):
    if request.method == 'DELETE':
            if pk is None:
                return Response({'error': 'Invalid request'}, status=400)
        
            else:
                task = Task.objects.get(pk=pk)
                
                task.delete()
                return Response({'status':'deleted'},status=status.HTTP_200_OK)
        
    