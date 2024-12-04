from django.urls import path

from app.views.PesquisaView import PesquisaView
from api.views import (
    ProdutoListAPIView, 
    ProdutoRetrieveAPIView, 
    ProdutoCreateAPIView, 
    
    UsuarioCreateAPIView, 
    UsuarioListAPIView,
    LoginAPIView,
    
    VendedorListAPIView
)

app_name = 'api'

urlpatterns = [
    path('produtos/', ProdutoListAPIView.as_view(), name='produto-list'),
    path('produtos/<int:pk>', ProdutoRetrieveAPIView.as_view(), name='produto-retrieve'),
    path('produtos/create/', ProdutoCreateAPIView.as_view(), name='produto-create'),
    
    path('usuario/', UsuarioListAPIView.as_view(), name='usuario-list'),
    path('usuario/create/', UsuarioListAPIView.as_view(), name='usuario-create'),
    path('usuario/login/', LoginAPIView.as_view(), name='usuario-login'),
    
    path('vendedores/', VendedorListAPIView.as_view(), name='vendedor-list'),
]
