from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render
from mercado.models.Produto import Produto
from django.db.models import Q

class ProdutoView(DetailView):
    template_name = "mercado/pages/produto-detalhe.html"

    def get_queryset(self):
        return super().get_queryset().get(Q(is_ativo=True))
    
    def get(self, request, id):
        produto = get_object_or_404(Produto, pk=id)

        context = {
            "produto": produto
        }

        return render(request, self.template_name, context)