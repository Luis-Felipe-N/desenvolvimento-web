from rest_framework import generics
from api.serializers import ProdutoSerializer
from app.models import Produto

class ProdutoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer