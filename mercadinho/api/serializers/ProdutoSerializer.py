from rest_framework import serializers
from app.models import Produto
from users.models import Vendedor
from api.serializers import ProdutoSerializer

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('id', 'nome_loja', 'nome_completo', 'cnpj', 'endereco', 'telefone')

class ProdutoSerializer(serializers.ModelSerializer):
    vendedor = VendedorSerializer(read_only=True)
    class Meta:
        model = Produto
        # fields = '__all__'
        fields = [
            'nome', 
            'descricao', 
            'descricao_html', 
            'is_descricao_html', 
            'is_ativo', 
            'preco', 
            'vendedor', 
            'imagem', 
            'categoria', 
            'desconto', 
            'com_desconto', 
            'data_criacao'
        ]