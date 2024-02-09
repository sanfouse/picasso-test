from celery import shared_task
from .models import File

@shared_task
def process_uploaded_file(file_id):
    File.objects.filter(id=file_id).update(processed=True, status_code='201')