from rest_framework import viewsets
from .models import Postagem ,Curtida ,Comentario
from .serializers import PostagemSerializer, CurtidaSerializer, ComentarioSerializer
from rest_framework.permissions import IsAuthenticated
from usuario.permissions import IsOutroTipo 

class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    permission_classes = [IsOutroTipo]

    def perform_create(self, serializer):
        # Atribuindo o usuário logado à postagem
        serializer.save(usuario=self.request.user)

class CurtidaViewSet(viewsets.ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer
    permission_classes = [IsAuthenticated] 
    
    def perform_create(self, serializer):
        print(self.request.data)
        # Associar o usuário logado ao objeto Curtida
        postagem = self.request.data.get('postagem')
        # Passa o usuário logado e o ID da postagem para o serializer
        serializer.save(usuario=self.request.user, postagem_id=postagem)


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Pegando os dados necessários diretamente da requisição
        postagem = self.request.data.get('postagem')
        conteudo = self.request.data.get('conteudo')

        if not postagem:
            raise serializer.ValidationError("O campo 'postagem' é obrigatório.")

        # Agora salvando diretamente com os dados adicionais
        serializer.save(usuario=self.request.user, postagem_id=postagem, conteudo=conteudo)