from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from restfilesupload.serializers import FileSerializer


class FileUploadViewSet(viewsets.ViewSet):

    def create(self, request):

        serializer_class = FileSerializer(data=request.data)
        if request.method == 'POST':
            if 'file' not in request.FILES or not serializer_class.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                handle_uploaded_file(request.FILES.getlist("file"))
                return Response(status=status.HTTP_201_CREATED)


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    class Meta:
        fields = ['pk' , 'file']

# # Create your views here.
# file = serializers.FileField(upload_to='images/')