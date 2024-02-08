docker-compose up -d
python manage.py migrate
celery -A file_processing_project worker -l info