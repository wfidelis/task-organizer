from django.contrib.auth.models import Inbox
from rest_framework import serializers

class InboxSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Inbox
        fields = ['task', 'description', 'created_at','updated_at','time_needed']
