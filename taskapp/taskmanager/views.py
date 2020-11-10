from taskmanager.models import Inbox
from taskmanager.serializers import InboxSerializer
from rest_framework import generics

class InboxList(generics.ListCreateAPIView):
        queryset = Inbox.objects.all()
        serializer_class = InboxSerializer


class InboxDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer



