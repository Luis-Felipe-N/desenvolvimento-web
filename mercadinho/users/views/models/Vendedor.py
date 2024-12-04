from django.db import models


class Vendedor(models.Model):

    username = models.OneToOneField(
        'Usuario',
        on_delete=models.CASCADE,
        null=True
    )

    nome_loja = models.CharField(
        verbose_name="Nome da loja",
        max_length=96
    )

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=96
    )

    cnpj = models.CharField(
        verbose_name="CNPJ sem formatação",
        help_text="CNPJ sem formatação",
        blank=False,
        null=False,
        max_length=14
    )

    endereco = models.CharField(
        verbose_name="Endereço",
        max_length=194
    )

    telefone = models.CharField(
        verbose_name="Telefone",
        max_length=11
    )

    def save(self, *args, **kwargs):
        self.nome_completo = self.username.get_full_name()
        return super(Vendedor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        db_table = "vendedor"

    def __str__(self):
        return self.nome_loja
