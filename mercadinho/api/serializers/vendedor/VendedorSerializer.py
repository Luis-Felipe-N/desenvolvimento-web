from rest_framework import serializers
from users.models import Vendedor
from api.serializers import ProdutoSerializer

class VendedorSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True, source='produto_set')

    class Meta:
        model = Vendedor
        fields = ('id', 'nome_loja', 'nome_completo', 'cnpj', 'endereco', 'telefone', 'produtos')
