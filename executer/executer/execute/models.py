from operator import mod
from django.db import models

# Create your models here.
class JobQueue(models.Model):
    
    class Status(models.TextChoices):
        PROCESSING = 'processing'
        CANCELLED = 'cancelled'
        COMPLETE = 'complete'
    
    status = models.CharField(choices=Status.choices, max_length=20, default=Status.PROCESSING)
    object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True, default=None)
    time_utilized = models.PositiveIntegerField(default=0)


class InProcessJob(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(JobQueue, on_delete=models.CASCADE)