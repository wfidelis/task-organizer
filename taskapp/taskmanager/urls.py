from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from taskmanager import views

urlpatterns = [
    path('tasks/', views.inbox_list, name='all_tasks'),
    path('tasks/<int:pk>/', views.inbox_details, name='task'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
