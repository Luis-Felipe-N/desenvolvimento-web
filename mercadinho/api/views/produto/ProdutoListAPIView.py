from rest_framework import generics
from api.serializers import ProdutoSerializer
from app.models import Produto
from django.db.models import Q

class ProdutoListAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        termo = self.request.query_params.get('query', None)

        print(termo)
        if termo:
            queryset = queryset.filter(
                Q(nome__icontains=termo) | Q(descricao__icontains=termo)
            )
            
        return queryset