from celery import shared_task
from .models import File
from file_processing_project.settings import MAX_FILE_SIZE
from django.core.files.storage import default_storage


@shared_task
def process_uploaded_file(file_id):
    status_code = '201'
    file_instance = File.objects.get(id=file_id)

    if default_storage.size(file_instance.file.name) > MAX_FILE_SIZE:
        status_code = '400'

    File.objects.filter(id=file_id).update(processed=True, status_code=status_code)
