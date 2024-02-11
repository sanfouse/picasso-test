from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    status_code = models.IntegerField(blank=True, null=True, default=400)