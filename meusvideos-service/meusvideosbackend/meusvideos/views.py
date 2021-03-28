import django_filters.rest_framework
from rest_framework import viewsets
from meusvideosbackend.meusvideos.models import Usuario, Video, Resenha
from meusvideosbackend.meusvideos.serializers import UsuarioSerializer, VideoSerializer, ResenhaSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """

    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset


class ResenhaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    queryset = Resenha.objects.all().order_by('id')
    serializer_class = ResenhaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'