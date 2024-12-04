from django.urls import path

from app.views.PesquisaView import PesquisaView
from api.views import ProdutoListAPIView, ProdutoRetrieveAPIView, ProdutoCreateAPIView

app_name = 'api'

urlpatterns = [
    path('produtos/', ProdutoListAPIView.as_view(), name='produto-list'),
    path('produtos/<int:pk>', ProdutoRetrieveAPIView.as_view(), name='produto-retrieve'),
    path('produtos/create/', ProdutoCreateAPIView.as_view(), name='produto-create'),
]
