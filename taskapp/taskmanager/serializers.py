from taskmanager.models import Inbox
from rest_framework import serializers


class InboxSerializer(serializers.ModelSerializer):


    class Meta:
        model = Inbox
        fields = ['task', 'description', 'created_at', 'updated_at', 'time_needed']
