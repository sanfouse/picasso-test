from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from .tasks import process_uploaded_file
from rest_framework import generics, views


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_file(request):
    file = request.data.get('file')

    if not file:
        return Response({'error': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = FileSerializer(data={'file': file})
    if serializer.is_valid():
        file_instance: File = serializer.save()
        process_uploaded_file.delay(file_instance.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FileListApiView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer