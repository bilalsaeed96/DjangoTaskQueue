from django.urls import path
from .views import GetTaskStatus, CreateTask, HealthCheck

urlpatterns = [
    path('health', HealthCheck.as_view(), name='health_check'),
    path('tasks', CreateTask.as_view(), name='create_task'),
    path('tasks/<int:pk>', GetTaskStatus.as_view(), name='project_vendor_profile'),
]
