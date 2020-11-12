from django.urls import path,include

urlpatterns = [
    path('', include('taskmanager.urls')),
    path('api-auth/', include('rest_framework.urls')),

    ]

