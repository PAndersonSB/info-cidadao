from rest_framework import generics, permissions ,status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UsuarioSerializer 
from rest_framework.views import APIView
from django.contrib.auth import authenticate

Usuario = get_user_model()

class RegistroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


class LoginUsuarioView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"detail": "Email e senha são obrigatórios"}, status=400)

        # Autenticar usuário com email e senha
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Gerar ou recuperar o token de autenticação
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key
            })
        else:
            return Response({"detail": "Credenciais inválidas"}, status=401)
