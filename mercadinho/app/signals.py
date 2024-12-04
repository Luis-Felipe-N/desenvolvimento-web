from django.db.models.signals import pre_save

from users.models.Vendedor import Vendedor
from users.models.Usuario import Usuario
from django.db.models.signals import pre_save, pre_delete

def criar_vendedor(sender, instance, **kwargs):
    usuario = Usuario.objects.get(id=instance.username.id)
    usuario.is_vendedor = True
    usuario.save()

    print(f'Criando vendedor ligado ao usuário [user]')


def remover_vendedor(sender, instance, **kwargs):
    usuario = Usuario.objects.get(id=instance.username.id)
    usuario.is_vendedor = False
    usuario.save()

pre_save.connect(criar_vendedor, sender=Vendedor)

pre_delete.connect(remover_vendedor, sender=Vendedor)