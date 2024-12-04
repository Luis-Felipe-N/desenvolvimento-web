from mercado.models.Categoria import Categoria
from mercado.models.Produto import Produto
from django.views.generic.list import ListView
from django.db.models import Q

class PesquisaView(ListView):
    template_name = 'mercado/pages/produtos.html'
    model = Produto
    context_object_name = 'produtos'

    def get_queryset(self):
        pesquisa_separada = self.request.GET.get('q').split(' ', 1)

        if len(pesquisa_separada) > 1:
            termo_pesquisa = pesquisa_separada[1]
            tipo_pesquisa = pesquisa_separada[0].split(":")[0]
        else:
            termo_pesquisa = pesquisa_separada[0]
            tipo_pesquisa = ''

        qs = Q()

        if tipo_pesquisa == 'categoria':
            slug_da_categoria = pesquisa_separada[0].split(":")[1]
            qs = Q(Q(categoria__slug=slug_da_categoria) & Q(is_ativo=True))
        elif tipo_pesquisa == 'meus-produtos':
            qs = Q(Q(vendedor__id=self.request.user.vendedor.id) & Q(is_ativo=True))


        return super().get_queryset().filter(Q(Q(nome__icontains=termo_pesquisa)) & qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pesquisa_pagina_atual = self.request.GET.get('q')
        pesquisa_separada = pesquisa_pagina_atual.split(' ', 1)

        if len(pesquisa_separada) > 1:
            termo_pesquisa = pesquisa_separada[1]
        else:
            termo_pesquisa = pesquisa_separada[0]

        context["titulo_da_pagina"] = f'Pesquisa por: {termo_pesquisa}'
        context["pesquisa_pagina_atual"] = pesquisa_pagina_atual

        return context