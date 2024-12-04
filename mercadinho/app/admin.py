from django.contrib import admin

from mercado.models import *

admin.site.register(Produto)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    pass