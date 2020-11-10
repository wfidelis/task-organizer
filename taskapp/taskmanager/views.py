from rest_framework import status
from rest_framework.response import Response
from taskmanager.models import Inbox
from taskmanager.serializers import InboxSerializer
from django.http import Http404
from rest_framework.views import APIView

class InboxList(APIView):
    '''
    List all tasks in the inbox or create a new task
    '''
    def get(self, request, format=None):
        all_tasks = Inbox.objects.all()
        serializer = InboxSerializer(all_tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InboxDetails(APIView):
    '''
    get, delete or update an inbox instance
    '''
    def get_object(self, pk):

        try:
            task = Inbox.objects.get(pk=pk)
        except Inbox.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        serializer = InboxSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = JSONParser().parse(request)
        serializer = InboxSerializer(all_tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

