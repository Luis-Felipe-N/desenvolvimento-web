from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from mercado.models.Produto import Produto
from mercado.forms.ProdutoForm import ProdutoForm


class EditarProdutoView(LoginRequiredMixin, UpdateView):
    template_name = template_name = 'mercado/pages/form-produto.html'
    model = Produto
    form_class = ProdutoForm

    # def get(self, request, id):
    #     produto = Produto.objects.get(Q(vendedor__id=self.request.user.vendedor.id) & Q(id=id))
    #     form = ProdutoForm(instance=produto)

    #     context = {
    #         "form": form
    #     }

    #     return render(request, self.template_name, context)

    def get_queryset(self):
        id = self.kwargs["pk"]
        
        return super().get_queryset().filter(Q(vendedor__id=self.request.user.vendedor.id) & Q(id=id))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_da_pagina"] = "Editar Produto"
        return context