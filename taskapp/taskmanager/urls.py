from django.urls import path
from taskmanager import views

urlpatterns = [
    path('tasks/', views.inbox_list, name='all_tasks'),
    path('tasks/<int:pk>/', views.inbox_details, name='task'),
]
