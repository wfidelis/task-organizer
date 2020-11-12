from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from taskmanager import views

urlpatterns = [
    path('tasks/', views.InboxList.as_view()),
    path('tasks/<int:pk>/', views.InboxDetails.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
