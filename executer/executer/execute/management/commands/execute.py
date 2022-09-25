import random
import asyncio
from django.db import transaction
from asgiref.sync import sync_to_async, async_to_sync
from executer.execute.models import JobQueue, InProcessJob
from django.core.management.base import BaseCommand
from time import sleep
import threading
from datetime import datetime, timedelta, timezone
from os import environ
from asyncio.exceptions import TimeoutError


class Command(BaseCommand):
    help = 'Schedule jobs after every 10 sec'

    def handle(self, *args, **options):
        pass
        asyncio.run(self.task_handler())

    async def task_handler(self):
        while True:
            thread = threading.Thread(target=self.run_task)
            thread.start()
            await asyncio.sleep(10)

    async def get_time(self):
        time = random.randint(15, 40)
        time_out = int(environ.get('MAX_TIMEOUT_SEC', 60))
        try:
            await asyncio.wait_for(asyncio.sleep(time), timeout=time_out)
        except TimeoutError:
            return (False, time_out)
        return (True, time)

    def clean_up(self):
        time_threshold = datetime.now()
        time_threshold = datetime.now(tz=timezone.utc) - timedelta(seconds=int(environ.get('MAX_TIMEOUT_SEC', 60)))
        results = InProcessJob.objects.filter(created_at__lte=time_threshold)
        results.delete()
    
    def run_task(self):
        job_id = None
        self.clean_up()
        with transaction.atomic():
            inprocess_ids = [job.job.id for job in InProcessJob.objects.all()]
            job = JobQueue.objects.select_for_update().filter(
                status=JobQueue.Status.PROCESSING
            ).exclude(
                id__in=inprocess_ids
            ).order_by('created_at').first()
            
            print(job)
            
            if not job or InProcessJob.objects.filter(job=job).exists():
                return
            
            time_delta = datetime.now(tz=timezone.utc) - timedelta(minutes=5)
            if JobQueue.objects.filter(
                object_id=job.object_id,
                completed_at__gte=time_delta,
                completed_at__lte=datetime.now(tz=timezone.utc)
            ).exists():
                return
            
            job_id = job.id
            InProcessJob.objects.create(job=job)
            
        time = async_to_sync(self.get_time)()
        job.status = JobQueue.Status.COMPLETE if time[0] else JobQueue.Status.CANCELLED
        job.time_utilized = time[-1]
        job.completed_at = datetime.now(tz=timezone.utc)
        job.save()