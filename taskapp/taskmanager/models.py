from django.db import models

class Inbox(models.Model):
    task = models.CharField(max_length = 255)
    description = models.TextField(max_length = None)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    time_needed = models.PositiveIntegerField()
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    
