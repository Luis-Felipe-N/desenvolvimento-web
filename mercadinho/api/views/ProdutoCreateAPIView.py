from rest_framework.generics import CreateAPIView
from app.models import Produto
from api.serializers import ProdutoSerializer

class ProdutoCreateAPIView(CreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
