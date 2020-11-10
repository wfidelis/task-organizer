from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from taskmanager.models import Inbox
from taskmanager.serializers import InboxSerializer

@api_view(['GET', 'POST'])
def inbox_list(request):
    '''
    List all tasks in the inbox or create a new task 
    '''
    if request.method == 'GET':
        all_tasks = Inbox.objects.all()
        serializer = InboxSerializer(all_tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def inbox_details(request, pk):
    '''
    get, delete or update a task
    '''
    try:
        task = Inbox.objects.get(pk=pk)
    except Inbox.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InboxSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InboxSerializer(all_tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

