from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

Usuario = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'tipo_usuario', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'].lower(),
            password=validated_data['password'],
            tipo_usuario=validated_data.get('tipo_usuario', 'cidadao'),
        )
        return user