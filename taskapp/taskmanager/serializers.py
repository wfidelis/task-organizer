from taskmanager.models import Inbox
from rest_framework import serializers
from django.contrib.auth.models import User

class InboxSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Inbox
        fields = ['task', 'description', 'created_at', 'updated_at', 'time_needed', 'owner']


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Inbox.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']
