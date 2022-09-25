from rest_framework import serializers
import executer.execute.models as models


class JobQueueSerializer(serializers.ModelSerializer):
    job_id = serializers.SerializerMethodField()

    class Meta:
        model = models.JobQueue
        fields = [
            'job_id',
            'status',
            'object_id',
            'created_at',
            'completed_at',
            'status',
            'time_utilized'
        ]
        read_only_fields = ['job_id', 'status', 'created_at', 'completed_at', 'status', 'time_utilized']
    
    def get_job_id(self, instance):
        return instance.id
