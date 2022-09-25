from rest_framework.generics import CreateAPIView
from executer.api.serializers import JobQueueSerializer
from executer.execute.models import JobQueue


class CreateTask(CreateAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class = JobQueueSerializer
