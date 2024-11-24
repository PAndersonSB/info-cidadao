from django.db import models
from django.conf import settings
from usuario.models import Usuario  

class Postagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Postagem de {self.usuario.email} - {self.data_criacao}'
    
    def get_comentarios(self):
        return self.comentarios.all()  # 'comentarios' é o related_name no modelo Comentario


class Curtida(models.Model): # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    data_curtida = models.DateTimeField(auto_now_add=True)

    # Garantindo que um usuário não possa curtir a mesma postagem mais de uma vez
    class Meta:
        unique_together = ['usuario', 'postagem']

    def __str__(self):
        return f"{self.usuario.username} curtiu {self.postagem.titulo}"
    

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)