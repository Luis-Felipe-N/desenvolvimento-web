from re import template
from django.shortcuts import redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from mercado.models.Carrinho import Carrinho
from mercado.models.Produto import Produto


# ver forma melhor de criar o Carrinho

class CarrinhoView(LoginRequiredMixin, ListView):
    template_name = 'mercado/pages/carrinho.html'
    model = Carrinho
    contect_object_name = 'produtos'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().filter(usuario__id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["titulo_da_pagina"] = "Carrinho"
        return context

class AddCarrinhoView(LoginRequiredMixin, View):
    model = Carrinho
    success_url = 'mercado:home'

    def get(self, request, produto_id):
        produto = Produto.objects.get(id=produto_id)
        usuario = request.user

        carrinho = Carrinho.objects.get_or_create(usuario=usuario, produto=produto)
        print(request)

        return redirect('mercado:carrinho')

    def post(self, request, produto_id):
        produto = Produto.objects.get(id=produto_id)
        usuario = request.user

        Carrinho.objects.create(usuario=usuario, produto=produto)

        return redirect('mercado:carrinho')

class RemoverCarrinhoView(LoginRequiredMixin, View):
    model = Carrinho
    success_url = 'mercado:home'

    def get(self, request, carrinho_id):
        carrinho = Carrinho.objects.get(id=carrinho_id, usuario=self.request.user)

        carrinho.delete()
        print(request)

        return redirect('mercado:carrinho')

