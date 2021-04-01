from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from meusvideosbackend.meusvideos.models import Usuario, Video, Resenha


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ModelField(model_field=Usuario()._meta.get_field('id'), required=False)

    class Meta:
        model = Usuario
        fields = ['id', "nome", "username", 'dtNasciemento']
        extra_kwargs = {
            'username': {'validators': []}
        }

    def existsByUsername(self, usuario):
        try:
            return Usuario.objects.get(pk=usuario.get("id"))
        except Usuario.DoesNotExist:
            raise ObjectDoesNotExist("Usuario não existe! Cadastre-se!")


class ResenhaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ModelField(model_field=Resenha()._meta.get_field('id'), required=False)

    class Meta:
        model = Resenha
        fields = ['id', 'texto']


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer(many=False)
    resenhas = ResenhaSerializer(many=True)
    id = serializers.ModelField(model_field=Video()._meta.get_field('id'), required=False)

    class Meta:
        model = Video
        fields = ['id', 'url', 'nome', 'usuario', 'resenhas']

    def create(self, validated_data, **keywords):
        usuarioSerializer = UsuarioSerializer()
        resenhas = validated_data.pop('resenhas')
        usuario = usuarioSerializer.existsByUsername(validated_data.pop('usuario'))
        video = Video.objects.create(usuario=usuario, **validated_data)
        for resenha in resenhas:
            resenhaInst, created = Resenha.objects.get_or_create(**resenha, video=video)
            video.resenhas.add(resenhaInst)
        return video

    def update(self, instance, validated_data):
        usuarioSerializer = UsuarioSerializer()
        resenhas = validated_data.pop('resenhas')
        usuario = usuarioSerializer.existsByUsername(validated_data.pop('usuario'))
        Video.objects.filter(pk=validated_data["id"]).update(**validated_data, usuario=usuario)
        video = Video.objects.get(pk=validated_data["id"])
        video.resenhas.filter(video=video).delete()
        for resenha in resenhas:
            resenhasInst, created = Resenha.objects.get_or_create(**resenha, video=video)
            video.resenhas.add(resenhasInst)
        return Video.objects.get(pk=validated_data["id"])
