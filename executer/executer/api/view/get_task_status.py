from rest_framework.generics import RetrieveAPIView
from executer.api.serializers import JobQueueSerializer
from executer.execute.models import JobQueue


class GetTaskStatus(RetrieveAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class = JobQueueSerializer
    queryset=JobQueue.objects.all()
