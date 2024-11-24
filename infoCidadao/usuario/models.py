from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    TIPOS_USUARIO = (
        ('cidadao', 'Cidadão'),
        ('outro', 'Nome ainda não definido para os usuario que farao postagem'),
    )

    tipo_usuario = models.CharField(max_length=10, choices=TIPOS_USUARIO, default='cidadao')

    # Use o email como identificador principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Campos obrigatórios além do email
    
    def is_cidadao(self):
        return self.tipo_usuario == 'cidadao'
    
    def is_outro_tipo(self):
        return self.tipo_usuario == 'outro'