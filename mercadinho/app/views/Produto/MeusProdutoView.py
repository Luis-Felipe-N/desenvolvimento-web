from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models import Q


from mercado.models.Produto import Produto

class MeusProdutoView(LoginRequiredMixin, ListView):
    template_name = 'mercado/pages/meus-produtos.html'
    model = Produto
    context_object_name = 'produtos'

    def get_queryset(self):
        return super().get_queryset().filter(Q(vendedor__id=self.request.user.vendedor.id) & Q(is_ativo=True))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quantidade_produto = Produto.objects.filter(Q(vendedor__id=self.request.user.vendedor.id))
        context["titulo_da_pagina"] = "Meus Produtos"
        context["pesquisa_pagina_atual"] = "meus-produtos "
        context["quantidade_produtos_ativos"] = quantidade_produto.filter( Q(is_ativo=True)).count  
        context["quantidade_produtos_desativos"] = quantidade_produto.filter( Q(is_ativo=False)).count 
        context["quantidade_produtos"] =quantidade_produto.count  
        return context
