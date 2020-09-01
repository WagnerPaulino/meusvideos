from rest_framework.response import Response
from rest_framework import viewsets
from meusvideosbackend.meusvideos.models import Usuario, Video, Resenha
from meusvideosbackend.meusvideos.serializers import UsuarioSerializer, VideoSerializer, ResenhaSerializer
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset


class ResenhaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    queryset = Resenha.objects.all().order_by('id')
    serializer_class = ResenhaSerializer