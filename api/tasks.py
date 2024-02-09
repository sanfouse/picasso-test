from celery import shared_task
from .models import File

@shared_task
def process_uploaded_file(file_id):
    ### проверка
    File.objects.filter(id=file_id).update(processed=True)