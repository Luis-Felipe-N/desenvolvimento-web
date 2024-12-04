from django.db import models

class Categoria(models.Model):
    nome = models.CharField(
        verbose_name="Categoria",
        max_length=96
    )

    slug = models.SlugField(
        verbose_name="Slug da categoria",
        unique=True,
        null=True
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria"

    def __str__(self):
        return self.nome