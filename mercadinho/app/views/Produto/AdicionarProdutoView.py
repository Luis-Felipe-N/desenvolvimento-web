from io import StringIO
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from django.views.generic.edit import CreateView
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
##############
from mercado.forms.ProdutoForm import ProdutoForm
from mercado.models.Produto import Produto

class AdicionarProdutoView(LoginRequiredMixin, CreateView):
    template_name = 'mercado/pages/form-produto.html'
    model = Produto
    form_class = ProdutoForm
    
    def dispatch(self, request, *args, **kwargs):
        print(request.user.is_vendedor)
        if request.user.is_vendedor is not True:
            messages.error(request, "Para adicionar um produto você precisa se tornar vendedor")
            return redirect('users:register-vendedor')
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        produto = form.save(commit=False)
        produto.vendedor = self.request.user.vendedor
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 

        context["titulo_da_pagina"] = "Adicionar produto"
        return context
