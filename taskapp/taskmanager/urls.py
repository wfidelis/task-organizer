from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from taskmanager import views

urlpatterns = [
    path('tasks/', views.InboxList.as_view(), name='all_tasks'),
    path('tasks/<int:pk>/', views.InboxDetails.as_view(), name='task'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
