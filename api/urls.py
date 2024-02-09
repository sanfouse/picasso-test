from django.urls import path
 
from . import views

app_name = 'api'
 
urlpatterns = [
    path('upload/', views.upload_file, name='upload'),
    path('files/', views.FileListApiView.as_view(), name='files')
]