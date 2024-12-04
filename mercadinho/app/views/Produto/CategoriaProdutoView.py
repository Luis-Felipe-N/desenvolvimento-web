from contextlib import ContextDecorator
from django.views.generic.list import ListView
from django.db.models import Q

from mercado.models.Produto import Produto
from mercado.models.Categoria import Categoria

class CategoriaProdutoView(ListView):
    template_name = 'mercado/pages/produtos.html'
    model = Produto
    context_object_name = 'produtos'
    
    def get_queryset(self):
        slug_da_categoria = self.kwargs["slug"]
        
        return super().get_queryset().filter(Q(Q(categoria__slug=slug_da_categoria) & Q(is_ativo=True)))    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(context["produtos"])

        slug = self.kwargs["slug"]
        try:
            categoria = Categoria.objects.get(slug=slug)
            titulo_da_pagina = f'Categoria: {categoria.nome}' 
        except:
            titulo_da_pagina = f'Categoria "{slug}" não foi encontrada'
            
        context["titulo_da_pagina"] = titulo_da_pagina
        context["pesquisa_pagina_atual"] = f'categoria:{slug}'

        return context
