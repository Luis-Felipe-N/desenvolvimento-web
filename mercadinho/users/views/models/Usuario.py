from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(
        verbose_name="Email do usuário",
        max_length=30,
        unique=True
    )

    is_vendedor = models.BooleanField(
        verbose_name="É um vendedor",
        default=False
    )

    perfil_imagem  = models.ImageField(
        upload_to="users/perfil/%Y/%m/%d/",
        null=True
    )

    # USERNAME_FIELD = 'email'