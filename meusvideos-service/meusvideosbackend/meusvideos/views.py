from django.shortcuts import render
from rest_framework import viewsets
from meusvideosbackend.meusvideos.models import Usuario, Video
from meusvideosbackend.meusvideos.serializers import UsuarioSerializer, VideoSerializer
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer