from django.urls import path

from app.views.PesquisaView import PesquisaView
from .views import *

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/category/<slug:slug>/', CategoriaProdutoView.as_view(), name="categoria-produto"),
    path('produto/all/', MeusProdutoView.as_view(), name="meus-produtos"),
    path('product/add/', AdicionarProdutoView.as_view(), name="adicionar-produto"),
    path('product/<int:pk>/edit', EditarProdutoView.as_view(), name="editar-produto"),
    path('product/<int:id>/', ProdutoView.as_view(), name="produto"),

    path('carrinho/', CarrinhoView.as_view(), name="carrinho"),
    path('carrinho/adicionar/<int:produto_id>', AddCarrinhoView.as_view(), name="adicionar-carrinho"),
    path('carrinho/remover/<int:carrinho_id>', RemoverCarrinhoView.as_view(), name="remover-carrinho"),

    path('search/', PesquisaView.as_view(), name="pesquisa")
]
