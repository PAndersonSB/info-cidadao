from rest_framework import serializers
from .models import Curtida, Postagem ,Comentario

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ['id', 'usuario', 'conteudo', 'data_criacao', 'curtidas']
        read_only_fields = ['usuario', 'data_criacao']

class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtida
        fields = ['usuario', 'postagem', 'data_curtida']

    usuario = serializers.StringRelatedField()
    postagem = serializers.StringRelatedField()

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['postagem', 'usuario', 'conteudo', 'data_criacao']
        read_only_fields = ['usuario', 'data_criacao']

    def create(self, validated_data):
        print(validated_data,"validate data")
        return super().create(validated_data)
    
    def validate_postagem(self, value):
        """Valida se a postagem existe antes de criar um comentário"""
        if not Postagem.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Postagem não encontrada.")
        return value