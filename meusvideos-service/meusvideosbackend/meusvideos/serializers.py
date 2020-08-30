from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from meusvideosbackend.meusvideos.models import Usuario, Video, Resenha

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'username', 'password', 'dtNasciemento']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def existsByUsername(self, usuario):
        try:
            return Usuario.objects.get(username=usuario.get("username"))
        except:
            raise ObjectDoesNotExist("Usuario não existe! Cadastre-se!")

class ResenhaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resenha
        fields = ['id', 'texto']

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer(many=False)
    resenhas = ResenhaSerializer(many=True)
    class Meta:
        model = Video
        fields = ['id', 'url', 'nome', 'usuario', 'resenhas']

    def create(self, validated_data):
        usuarioSerializer = UsuarioSerializer()
        resenhas = validated_data.pop('resenhas')
        usuario = usuarioSerializer.existsByUsername(validated_data.pop('usuario'))
        video = Video.objects.create(usuario=usuario, **validated_data)
        for resenha in resenhas:
            Resenha.objects.create(video=video, **resenha)
        return video