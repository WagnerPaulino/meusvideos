from rest_framework import serializers
from meusvideosbackend.meusvideos.models import Usuario, Video

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'username', 'password', 'dtNasciemento']

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'url', 'nome', 'resenha', 'usuario']