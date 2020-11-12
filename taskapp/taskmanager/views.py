from rest_framework import permissions
from taskmanager.models import Inbox
from taskmanager.serializers import InboxSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from taskmanager.serializers import UserSerializer

class InboxList(generics.ListCreateAPIView):
        queryset = Inbox.objects.all()
        serializer_class = InboxSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class InboxDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
