from io import BytesIO
from django.urls import reverse
from django.db import models
from django.core.files.base import ContentFile
import locale
from PIL import Image
from mercado.models.Categoria import Categoria

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        blank=False,
        null=False,
        max_length=96,
        help_text='Ex: Motorola Moto g10',
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        help_text="Ex: Este é o melhor produto do mundo"
    )

    descricao_html = models.TextField(
        verbose_name="Descrição em HTML",
        help_text="Ex: <h1>Este é o melhor produto do mundo</h1>",
        blank=True,
        null=True
    )

    is_descricao_html = models.BooleanField(
        default=False
    )

    is_ativo = models.BooleanField(default=False)

    preco = models.FloatField(
        verbose_name="Preço",
        blank=False,
        null=False,

    )

    vendedor = models.ForeignKey(
        'users.Vendedor',
        on_delete=models.CASCADE,
        null=True,
    )

    imagem = models.ImageField(upload_to="mercado/covers/%Y/%m/%d/")

    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True
    )

    desconto = models.FloatField(
        verbose_name="Porcentagem do desconto",
        blank=True,
        null=True
    )

    com_desconto = models.BooleanField(
        verbose_name="O Produto está com desconto",
        blank=True
    )

    data_criacao = models.DateField(
        verbose_name="Data de criação",
        auto_now=True,
    )

    def save(self, *args, **kwargs):
        if self.descricao_html:
            self.is_descricao_html = True
        else:
            self.is_ativo = True

        pil_image_obj = Image.open(self.imagem)
        pil_image_obj.thumbnail((100, 100), Image.ANTIALIAS)

        new_image_io = BytesIO()
        pil_image_obj.save(new_image_io, pil_image_obj.format)

        temp_name = self.imagem.name
        self.imagem.delete(save=False)  

        self.imagem.save(
            temp_name,
            content=ContentFile(new_image_io.getvalue()),
            save=False
        )

        
        return super(Produto, self).save(*args, **kwargs)   

    def get_absolute_url(self, **kwargs):
        return reverse('mercado:produto', kwargs={'id': self.id})
    
    def get_preco_formatado(self, preco):
        locale.setlocale( locale.LC_ALL, '' )
        preco_formatado = locale.currency(preco, symbol=False, grouping=True)
        return preco_formatado

    def get_preco(self, *args, **kwargs):
        preco_formatado = self.get_preco_formatado(self.preco)
        return preco_formatado

    def get_quantidade_desconto(self, *args, **kwargs):
        desconto = self.desconto
        return f'{int(desconto)}%'

    def get_preco_com_desconto(self, *args, **kwargs):
        if self.desconto is None:
            preco_formatado = self.get_preco(   )
        else:
            desconto_em_reais = self.preco * (self.desconto / 100)

            preco_desconto = self.preco - desconto_em_reais

            preco_formatado = self.get_preco_formatado(preco_desconto)

        return preco_formatado

    def __str__(self):
        return self.nome