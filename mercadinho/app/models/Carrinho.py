from hashlib import blake2s
from django.db import models

class Carrinho(models.Model):
    usuario = models.ForeignKey(
        'users.Usuario',
        on_delete=models.CASCADE
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True,
        # auto_created=True,
        verbose_name="Data de criação"
    )

    produto = models.ForeignKey(
        'mercado.Produto',
        on_delete=models.CASCADE
    )

    quantidade = models.IntegerField(
        verbose_name="Quantidade",
        default=1,
        blank=False,
        null=False
    )

    def get_preco_total_produto(self):
        if self.produto.com_desconto is True:
            desconto_em_reais = self.produto.preco * (self.produto.desconto / 100)
            preco_produto = self.produto.preco - desconto_em_reais
        else:
            preco_produto = self.produto.preco

        preco_produto_final = preco_produto * self.quantidade

        return self.produto.get_preco_formatado(preco_produto_final)

    def __str__(self):
        return self.produto.nome