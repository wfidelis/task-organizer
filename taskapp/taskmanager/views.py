from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from taskmanager.models import Inbox
from taskmanager.serializers import InboxSerializer
from django.contrib.auth.decorators import login_required

@login_required
def inbox_list(request):
    '''
    List all tasks in the inbox or create a new task 
    '''
    if request.method == 'GET':
        all_tasks = Inbox.objects.all()
        serializer = InboxSerializer(all_tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

@login_required
def inbox_details(request, pk):
    '''
    get, delete or update a task
    '''
    try:
        task = Inbox.objects.get(pk=pk)
    except Inbox.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InboxSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InboxSerializer(all_tasks, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    
    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)
